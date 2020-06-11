from rest_framework import serializers
from .models import *


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = [
            'value',
            'max_points',
            'for_what',
            'note'
        ]
        extra_kwargs = {
            'value': {'required': False, 'allow_null': True},
            'max_points': {'required': False, 'allow_null': True},
            'for_what': {'required': False, 'allow_null': True},
            'note': {'required': False, 'allow_null': True},
        }
