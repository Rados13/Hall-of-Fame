from rest_framework import generics, mixins, status
from .serializers import CustomUserSerializer
from .permissions import IsOwnerOrReadOnly, IsAdmin
from rest_framework.permissions import IsAdminUser
from ..models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from groups.api.permissions import get_id_from_token


class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
    search_fields = ['first_name']
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self):
        queryset = User.objects.all()
        if self.kwargs.get("type") == "lectures":
            queryset = User.objects.filter(is_lecture=True)
        if self.kwargs.get("type") == "students":
            queryset = User.objects.filter(is_student=True)
        return queryset

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serialized = self.get_serializer(obj).data
        serialized['is_lecture'] = obj.is_lecture
        serialized['is_student'] = obj.is_student
        serialized['is_admin'] = obj.is_staff
        serialized.pop('password', None)
        return Response(serialized, status=status.HTTP_200_OK)

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        data = request.data['user']
        if 'is_lecture' in data:
            obj.is_lecture = data['is_lecture']
        if 'is_student' in data:
            obj.is_student = data['is_student']
        if 'is_admin' in data:
            obj.is_staff = data['is_admin']
        if 'is_active' in data:
            obj.is_active = data['is_active']
        obj.save()
        return Response("OK", status.HTTP_200_OK)


class UserInfo(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        obj = list(User.objects.filter(pk=get_id_from_token(request)))[0]
        info = {'is_lecture': obj.is_lecture, 'is_student': obj.is_student, 'is_admin': obj.is_superuser}
        return Response(info, status=status.HTTP_200_OK)
