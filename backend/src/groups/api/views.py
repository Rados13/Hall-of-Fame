from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .serializers import GroupSerializer,EnrolledSerializer
from djongo.models import Q
from .permissions import IsOwnerOrReadOnly
from groups.models import Group, Enrolled
import jwt
from HallOfFame.settings import SECRET_KEY
from rest_framework.renderers import JSONRenderer


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
        print(request.data)
        serializer = self.get_serializer()
        result = serializer.create(request.data)
        if result != None:
            result.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class StudentInGroupRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = []

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        print(request.data)
        obj = self.get_object()
        obj.enrolled_list.append(self.create_student(request))
        serializer = self.get_serializer(data = self.get_serializer(obj).data)
        if serializer.is_valid():
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_student(self, request):
        bearerToken = str(request.data['headers']['Authorization'])
        token = bearerToken[bearerToken.find(' ') + 1:]
        person = jwt.decode(token, SECRET_KEY)
        personID = person['user_id']
        return Enrolled(user_id=personID,marks_list=[],inattendances_list=[])
