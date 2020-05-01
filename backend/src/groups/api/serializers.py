from rest_framework import serializers


# from ..models import CustomUser
from groups.models import *


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = [
            'lecture_id',
            'main_lecture',
        ]


class DayTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayTime
        fields = [
            'day_of_week',
            'time',
        ]


class InattendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inattendence
        fields = [
            'class_num',
            'justified',
        ]
        extra_kwargs = {
            'class_num': {'required': False, 'allow_null': True},
            'justified': {'required': False, 'allow_null': True},
        }

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = [
            'value',
            'for_what',
            'note'
        ]
        extra_kwargs = {
            'value': {'required': False, 'allow_null': True},
            'for_what': {'required': False, 'allow_null': True},
            'note': {'required': False, 'allow_null': True},
        }

class EnrolledSerializer(serializers.ModelSerializer):
    inattendances_list = serializers.ListField(child=InattendenceSerializer(),allow_null=True)
    marks_list = serializers.ListField(child=MarkSerializer(),allow_null=True)

    class Meta:
        model = Enrolled
        fields = [
            'user_id',
            'inattendances_list',
            'marks_list'
        ]
        extra_kwargs = {
            'user_id': {'required': True, 'allow_null': False},
            'inattendances_list': {'required': False, 'allow_null': True},
            'marks_list': {'required': False, 'allow_null': True},
        }



class GroupSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    lectures_list = serializers.ListField(child=LectureSerializer())
    date_time = serializers.ListField(child=DayTimeSerializer(),allow_null=True)
    enrolled_list = serializers.ListField(child=EnrolledSerializer(),allow_null=True)

    class Meta:
        model = Group
        fields = [
            # 'uri',
            'pk',
            'course',
            'date_time',
            'lectures_list',
            'enrolled_list',
        ]
        extra_kwargs = {
            'date_time': {'required': False, 'allow_null': True},
            'lectures_list': {'required': False, 'allow_null': True},
            'enrolled_list': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        course = validated_data['course']
        date_time = []
        for elem in validated_data['date_time']:
            date_time.append(DayTime(**elem))
        lectures_list = []
        for elem in validated_data['lectures_list']:
            lectures_list.append(Lecture(**elem))
        enrolled_list = []
        user_obj = Group(course=course,
                         date_time=date_time,
                         lectures_list=lectures_list,
                         enrolled_list=enrolled_list)
        return user_obj

    def update(self, instance, validated_data):
        if 'course' in validated_data:
            instance.course = validated_data['course']
        if 'date_time' in validated_data:
            instance.date_time = list(map(lambda elem: DayTime(**elem), validated_data['date_time']))
        if 'lectures_list' in validated_data:
            instance.lectures_list = list(map(lambda elem: Lecture(**elem), validated_data['lectures_list']))
        if 'enrolled_list' in validated_data:
            instance.enrolled_list = list(map(lambda elem: Enrolled(*elem), validated_data['enrolled_list']))
        return instance




    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_uri(request)



