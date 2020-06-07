from rest_framework import serializers
from .models import *


class DayTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayTime
        fields = [
            'day_of_week',
            'time',
        ]
