from rest_framework import serializers
from users.models import User
from groups.models import *


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = [
            'lecture',
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


class EnrolledSerializer(serializers.ModelSerializer):
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


class GroupSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    lectures_list = serializers.ListField(child=LectureSerializer())
    date_time = serializers.ListField(child=DayTimeSerializer(), allow_null=True)
    enrolled_list = serializers.ListField(child=EnrolledSerializer(), allow_null=True)

    class Meta:
        model = Group
        fields = [
            # 'uri',
            'pk',
            'course',
            'date_time',
            'lectures_list',
            'enrolled_list',
            'course_end'
        ]
        extra_kwargs = {
            'date_time': {'required': False, 'allow_null': True},
            'lectures_list': {'required': False, 'allow_null': True},
            'enrolled_list': {'required': False, 'allow_null': True},
            'course_end': {'required': False, 'default': False}
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
        print(validated_data)
        if 'course' in validated_data:
            instance.course = validated_data['course']
        if 'date_time' in validated_data:
            instance.date_time = list(map(lambda elem: DayTime(**elem), validated_data['date_time']))
        if 'lectures_list' in validated_data:
            for elem in validated_data['lectures_list']:
                elem.pop('first_name', None)
                elem.pop('last_name', None)
            instance.lectures_list = list(map(
                lambda elem: Lecture(lecture=User.objects.get(pk=elem['id']), **elem),
                validated_data['lectures_list']))
        if 'enrolled_list' in validated_data:
            instance.enrolled_list = list(map(lambda elem: self.create_enrolled_from_json(**elem),
                                              validated_data['enrolled_list']))
        return instance


    def create_enrolled_from_json(self, *args, **kwargs):
        user = User.objects.filter(pk=kwargs.get('student'))[0]
        return Enrolled(
            student=user,
            inattendances_list=list(map(lambda elem: Inattendence(**elem), kwargs.get('inattendances_list'))),
            marks_list=list(map(lambda elem: Mark(**elem), kwargs.get('marks_list')))
        )

    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_uri(request)
