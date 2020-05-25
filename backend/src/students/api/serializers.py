from rest_framework import serializers
from students.models import StudentGroups
from lectures.api.serializers import PartGroupSerializer
from groups.api.serializers import UserSerializer


class StudentGroupsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    groups_list = serializers.ListField(child=PartGroupSerializer(), allow_null=True)

    class Meta:
        model = StudentGroups
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
        obj = list(StudentGroups.objects.filter(user_id=user.pk))
        if not obj:
            obj = StudentGroups(user=user)
        else:
            obj = obj[0]

        obj.groups_list.add(group)
        return obj
