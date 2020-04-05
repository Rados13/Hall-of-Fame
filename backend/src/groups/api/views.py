from rest_framework import generics, mixins
from .serializers import GroupSerializer
from djongo.models import Q
from .permissions import IsOwnerOrReadOnly
from groups.models import Group


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
        return self.create(request, *args, **kwargs)


class GroupRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Group.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
