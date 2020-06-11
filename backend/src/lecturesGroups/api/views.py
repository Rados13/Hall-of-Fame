from groups.api.permissions import ReadOnly, get_id_from_token
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .serializers import *
from lecturesGroups.models import LectureGroups
from rest_framework.permissions import IsAdminUser


class LecturesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = LectureGroupsSerializer
    permission_classes = [ReadOnly, IsAdminUser]

    def get(self, request, *args, **kwargs):
        queryset = list(LectureGroups.objects.all())
        obj = queryset[0]
        result = {'user': UserSerializer(obj.user).data,
                  'groupsSecond': [PartGroupSerializer(elem).data for elem in obj.groups_list.all()]}
        return Response(result, status=status.HTTP_200_OK)


class LectureRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = LectureGroupsSerializer
    permission_classes = [ReadOnly]

    def get(self, request, *args, **kwargs):
        obj = self.get_object_filter(get_id_from_token(request))
        if obj is None:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        result = [PartGroupSerializer(elem).data for elem in obj.groups_list.all()]
        return Response(result, status=status.HTTP_200_OK)

    def get_queryset(self):
        return LectureGroups.objects.all()

    def get_object_filter(self, pk):
        result = list(LectureGroups.objects.filter(user_id=pk))
        return result[0] if result != [] else None
