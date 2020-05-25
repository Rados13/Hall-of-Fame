from groups.queries import Querying
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .serializers import GroupSerializer
from djongo.models import Q
from .permissions import *
from groups.models import Group, Enrolled, Mark
from ..stats import *
from students.api.serializers import StudentGroupsSerializer
from lectures.api.serializers import LectureGroupsSerializer


def get_lectures_names_in_dict(elem):
    return list(
        map(lambda x: {'first_name': x.lecture.first_name, 'last_name': x.lecture.last_name, 'id': x.lecture.pk},
            elem.lectures_list))


def get_student_names_in_dict(elem):
    return list(
        map(lambda x: {'first_name': x.student.first_name, 'last_name': x.student.last_name,
                       'id': x.student.pk},
            elem.enrolled_list))


class GroupAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [ReadOnly]

    def get(self, request, *args, **kwargs):
        queryset = Group.objects.all()
        result = [self.get_serializer(elem).data for elem in list(queryset)]
        for elem in result:
            elem.pop('enrolled_list', None)
        return Response(result, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Group.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            queryset = queryset.filter(Q(name__icontains=query)).distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        user = get_user_from_request(request)
        request.data['lectures_list'] = [{'lecture': user, 'main_lecture': True}]
        result = serializer.create(request.data)
        if result is not None:
            result.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [IsLectureOrReadOnly]

    def get(self, request, *args, **kwargs):
        obj = self.get_object()

        elem_serialized = self.get_serializer(obj).data

        if IsLecture().has_object_permission(request, self, obj):
            return Response(elem_serialized, status=status.HTTP_200_OK)
        elif IsStudent().has_object_permission(request, self, obj):
            id = get_id_from_token(request)
            elem_serialized['enrolled_list'] = [filter(
                lambda elem: elem['student']['pk'] == id, elem_serialized['enrolled_list']), ]
            return Response(elem_serialized, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer()
        obj = serializer.update(obj, request.data['group'])
        serializer = self.get_serializer(obj)
        serializer = self.get_serializer(data=serializer.data)
        if serializer.is_valid(raise_exception=True):
            for elem in obj.lectures_list:
                tmp = LectureGroupsSerializer().create({"user": elem.lecture,"group": obj})
                print(tmp)
                tmp.save()
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentInGroupRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = []

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        user = get_user_from_request(request)

        if not user.is_student:
            return Response("You are not student so you can't sign for course", status=status.HTTP_400_BAD_REQUEST)
        if user in obj.enrolled_list:
            return Response("You are already sign for that course", status=status.HTTP_400_BAD_REQUEST)

        obj.enrolled_list.append(Enrolled(student=user))
        serializer = self.get_serializer(data=self.get_serializer(obj).data)
        if serializer.is_valid():
            student_groups = StudentGroupsSerializer().create(
                {"user": get_user_from_request(request), "group": self.get_object()})
            if student_groups is None:
                return Response(None, status=status.HTTP_400_BAD_REQUEST)
            student_groups.save()
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkAllPostView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [IsLecture, PostMethod]

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        request = request.data
        marks = request['student_marks']
        mark_name = request['mark_name']
        max_points = request['max_points']
        obj.enrolled_list = list(
            map(lambda elem: self.append_mark_to_student(elem, marks, mark_name, max_points), obj.enrolled_list))

        serializer = self.get_serializer(data=self.get_serializer(obj).data)
        if serializer.is_valid():
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_mark_to_student(self, student, marks, mark_name, max_points):
        student.marks_list.append(Mark(for_what=mark_name, **marks[str(student.student.pk)], max_points=max_points))
        return student


class StatsAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [ReadOnly, IsLecture]

    def get(self, request, *args, **kwargs):
        groups_id = request.GET.getlist('groups_id[]')
        groups_id = list(map(lambda elem: int(elem), groups_id))

        obj = Querying(Group.objects, groups_id)
        marks = obj.filter_group_list()

        marks_names = obj.get_for_what_list()
        result = avg_points_for_what(marks, list(marks_names))

        students = obj.get_student_list()
        result['total'] = avg_points_all_students(students)

        result['link'] = plot_data(str(groups_id) + "stats", result, request.get_host())

        return Response(result, status=status.HTTP_200_OK)


class FinalGradeAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [IsLecture, PostMethod]

    def get_queryset(self):
        return Group.objects.all()

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.enrolled_list = final_grade_for_all_students(obj.enrolled_list)
        serializer = self.get_serializer(data=self.get_serializer(obj).data)
        if serializer.is_valid():
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
