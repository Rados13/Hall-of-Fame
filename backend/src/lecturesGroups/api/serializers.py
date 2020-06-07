from rest_framework import serializers
from lecturesGroups.models import LectureGroups
from groups.models import *
from groups.api.serializers import GroupSerializer, UserSerializer


class PartGroupSerializer(GroupSerializer):
    class Meta:
        model = Group
        fields = [
            'pk',
            'course',
            'date_time',
            'lectures_list',
            'course_end'
        ]
        extra_kwargs = {
            'date_time': {'required': False, 'allow_null': True},
            'lectures_list': {'required': False, 'allow_null': True},
            'course_end': {'required': False, 'default': False}
        }


class LectureGroupsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    groups_list = serializers.ListField(child=PartGroupSerializer(), allow_null=True)

    class Meta:
        model = LectureGroups
        fields = [
            # 'uri',
            'pk',
            'user',
            'groups_list',
        ]
        extra_kwargs = {
            'groups_list': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        user = validated_data['user']
        group = validated_data['group']
        obj = list(LectureGroups.objects.filter(user_id=user.pk))
        if not obj:
            obj = LectureGroups(user=user)
        else:
            obj = obj[0]

        obj.groups_list.add(group)
        return obj
