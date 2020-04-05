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
            'day_of_week'
            'time',
        ]

class InattendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inattendence
        fields = [
            'class_num',
            'justified',
        ]


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inattendence
        fields = [
            'value',
            'for_what',
            'note'
        ]


class EnrolledSerializer(serializers.ModelSerializer):
    inattendances_list = serializers.ListField(child = InattendenceSerializer())
    marks_list = serializers.ListField(child = MarkSerializer())

    class Meta:
        model = Enrolled
        fields = [
            'user_id',
            'inattendances_list',
            'marks_list'
        ]


class GroupSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    lecturers_list = serializers.ListField(child = LectureSerializer())
    date_time = serializers.ListField(child = DayTimeSerializer())
    enrolled_list = serializers.ListField(child = EnrolledSerializer() )
    class Meta:
        model = Group
        fields = [
            # 'uri',
            'pk',
            'course',
            'date_time',
            'lecturers_list',
            'enrolled_list',
        ]
        extra_kwargs = {
            'date_time': {'required': False, 'allow_null': True},
            'lecturers_list': {'required': False, 'allow_null': True},
            'enrolled_list': {'required': False, 'allow_null': True},
        }

    # def create(self, validated_data):
    #     course = validated_data['course']
    #     date_time = validated_data['date_time']
    #     lectures_list = validated_data['lectures_list']
    #     enrolled_list = validated_data['enrolled_list']
    #     user_obj = Group(course=course,
    #                      date_time=date_time,
    #                      lectures_list=lectures_list,
    #                      enrolled_list=enrolled_list)
    #     user_obj.save()
    #     return validated_data

    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_uri(request)

    # def validate_name(self, value):
    #     qs = User.objects.filter(name_iexact=value)
    #     if self.instance:
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exist():
    #         raise serializers.ValidationError("The name is already used")
    # convert to JSON
    # validations data
