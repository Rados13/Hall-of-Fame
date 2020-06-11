from rest_framework import generics, mixins, status
from .serializers import CustomUserSerializer
from .permissions import IsOwnerOrReadOnly
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
        return queryset

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        if 'is_lecture' in request.data:
            obj.is_lecture = request.data['is_lecture']
        if 'is_student' in request.data:
            obj.is_lecture = request.data['is_student']
        obj.save()


class UserInfo(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        obj = list(User.objects.filter(pk=get_id_from_token(request)))[0]
        info = {'is_lecture': obj.is_lecture, 'is_student': obj.is_student, 'is_admin': obj.is_superuser}
        return Response(info, status=status.HTTP_200_OK)
