from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .serializers import GroupSerializer, EnrolledSerializer, DayTimeSerializer, LectureSerializer
from djongo.models import Q
from .permissions import IsOwnerOrReadOnly
from groups.models import Group, Enrolled, Lecture,DayTime
import jwt
from HallOfFame.settings import SECRET_KEY


def get_id_from_token(request):
    bearerToken = str(request.data['headers']['Authorization'])
    token = bearerToken[bearerToken.find(' ') + 1:]
    person = jwt.decode(token, SECRET_KEY)
    return person['user_id']





class GroupAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]

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
        if result != None:
            result.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer()
        obj = serializer.update(obj,request.data['group'])
        serializer = self.get_serializer(obj)
        serializer = self.get_serializer(data = serializer.data)
        if serializer.is_valid(raise_exception=True):
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        print(serializer.data)
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
