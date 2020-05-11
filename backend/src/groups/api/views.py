from groups.queries import Querying
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import GroupSerializer
from djongo.models import Q
from .permissions import IsLecture, IsStudent, ReadOnly, get_id_from_token, PostMethod, get_request_data
from groups.models import Group, Enrolled, Mark
from users.models import User
from ..stats import *
# import json

def find_user_and_add_user_name(user, param_name):
    user_names = list(User.objects.filter(pk=user[param_name]))[0]
    user['first_name'] = user_names.first_name
    user['last_name'] = user_names.last_name
    return user


class GroupAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [ReadOnly]

    def get(self, request, *args, **kwargs):
        queryset = Group.objects.all()
        result = []
        for elem in queryset:
            elem.enrolled_list = []
            elem_serialized = self.get_serializer(elem).data
            elem_serialized['lectures_list'] = list(map(
                lambda x: find_user_and_add_user_name(x, 'lecture_id'), elem_serialized['lectures_list']))
            result.append(elem_serialized)
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
        request.data['lectures_list'] = [{'lecture_id': get_id_from_token(request), 'main_lecture': True}]
        result = serializer.create(request.data)
        if result is not None:
            result.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatsAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [ReadOnly, IsLecture]

    def get(self, request, *args, **kwargs):
        groups_id = request.GET.getlist('groups_id[]')
        groups_id = list(map(lambda elem: int(elem), groups_id))

        obj = Querying(Group.objects,groups_id)
        marks = obj.filter_group_list()

        marks_names = obj.get_for_what_list()
        result = avg_points_for_what(marks,list(marks_names))

        students = obj.get_student_list()
        result['total']=avg_points_all_students(students)

        # groups = list(chain.from_iterable(groups))
        # print(groups)
        # print(len(groups))

        return Response(result , status=status.HTTP_200_OK)
        # return Response("Hell yead" , status=status.HTTP_200_OK)


class GroupRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        elem_serialized = self.get_serializer(obj).data

        elem_serialized['lectures_list'] = list(map(
            lambda x: find_user_and_add_user_name(x, 'lecture_id'), elem_serialized['lectures_list']))
        elem_serialized['enrolled_list'] = list(map(
            lambda x: find_user_and_add_user_name(x, 'user_id'), elem_serialized['enrolled_list']))

        if IsLecture().has_object_permission(request, self, obj):
            return Response(elem_serialized, status=status.HTTP_200_OK)
        elif IsStudent().has_object_permission(request, self, obj):
            id = get_id_from_token(request)
            elem_serialized.enrolled_list = [filter(
                lambda elem: elem.user_id == id, elem_serialized['enrolled_list']), ]
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
        obj.enrolled_list.append(self.create_student(request))
        serializer = self.get_serializer(data=self.get_serializer(obj).data)
        if serializer.is_valid():
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_student(self, request):
        return Enrolled(user_id=get_id_from_token(request), marks_list=[], inattendances_list=[])


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
        print(request)
        marks = request['student_marks']
        mark_name = request['mark_name']

        obj.enrolled_list = list(
            map(lambda elem: self.append_mark_to_student(elem, marks, mark_name), obj.enrolled_list))

        serializer = self.get_serializer(data=self.get_serializer(obj).data)
        if serializer.is_valid():
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_mark_to_student(self, student, marks, mark_name):
        student.marks_list.append(Mark(for_what=mark_name, **marks[str(student.user_id)]))
        return student
