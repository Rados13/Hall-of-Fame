from rest_framework import generics, mixins
from .serializers import CustomUserSerializer
from djongo.models import Q
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from ..models import CustomUser


class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer

    # permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        # queryset = CustomUser.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            queryset = queryset.filter(Q(name__icontains=query)).distinct()
        return queryset

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
        return get_user_model().objects.all()
        # return CustomUser.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return CustomUser.objects.all(pk=pk)
