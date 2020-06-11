from inattendances.serializers import InattendenceSerializer
from marks.serializers import MarkSerializer
from rest_framework import serializers
from users.api.serializers import UserSerializer
from users.models import User
from .models import *


class EnrolledSerializer(serializers.ModelSerializer):
    student = UserSerializer()
    inattendances_list = serializers.ListField(child=InattendenceSerializer(), allow_null=True)
    marks_list = serializers.ListField(child=MarkSerializer(), allow_null=True)

    class Meta:
        model = Enrolled
        fields = [
            'student',
            'final_grade',
            'inattendances_list',
            'marks_list'
        ]
        extra_kwargs = {
            'student': {'required': True, 'allow_null': False},
            'final_grade': {'required': False, 'allow_null': True},
            'inattendances_list': {'required': False, 'allow_null': True},
            'marks_list': {'required': False, 'allow_null': True},
        }
