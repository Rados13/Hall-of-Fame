from rest_framework import serializers
from users.api.serializers import UserSerializer

from .models import *



class LectureSerializer(serializers.ModelSerializer):
    lecture = UserSerializer()

    class Meta:
        model = Lecture
        fields = [
            'lecture',
            'main_lecture',
        ]