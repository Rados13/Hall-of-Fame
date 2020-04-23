from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer
from djongo.models import Q
from .permissions import IsOwnerOrReadOnly
# from django.contrib.auth import get_user_model
from ..models import User
from rest_framework.filters import SearchFilter, OrderingFilter


class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
    search_fields = ['first_name']
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self):
        queryset = User.objects.all()
        result = []
        perms = IsOwnerOrReadOnly()
        for elem in queryset:
            if perms.has_object_permission(self.request,self,elem):
                result.append(elem)
        return result
        # return queryset

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return self.update (request, *args, **kwargs)


class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # queryset = Student.objects.all()

    def get_queryset(self):
        return User.objects.all()
        # return CustomUser.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return CustomUser.objects.all(pk=pk)
