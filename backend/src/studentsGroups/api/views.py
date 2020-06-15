from groups.api.permissions import ReadOnly, get_id_from_token
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAdminUser


class StudentsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = StudentGroupsSerializer
    permission_classes = [ReadOnly, IsAdminUser]

    def get_queryset(self):
        return StudentGroups.objects.all()

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        queryset = StudentGroups.objects.filter(user_id=pk)
        if len(queryset) == 0:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        obj = queryset[0]
        result = [PartGroupSerializer(elem).data for elem in obj.groups_list.all()]
        return Response(result, status=status.HTTP_200_OK)


class StudentRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = StudentGroupsSerializer
    permission_classes = [ReadOnly]

    def get(self, request, *args, **kwargs):
        obj = self.get_object_filter(get_id_from_token(request))
        if obj is None:
            return Response([], status=status.HTTP_204_NO_CONTENT)
        result = [PartGroupSerializer(elem).data for elem in obj.groups_list.all()]
        return Response(result, status=status.HTTP_200_OK)

    def get_queryset(self):
        return StudentGroups.objects.all()

    def get_object_filter(self, pk):
        result = list(StudentGroups.objects.filter(user_id=pk))
        return result[0] if result != [] else None
