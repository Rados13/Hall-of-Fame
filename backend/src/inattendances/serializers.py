from rest_framework import serializers
from .models import *


class InattendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inattendance
        fields = [
            'class_num',
            'justified',
        ]
        extra_kwargs = {
            'class_num': {'required': False, 'allow_null': True},
            'justified': {'required': False, 'allow_null': True},
        }