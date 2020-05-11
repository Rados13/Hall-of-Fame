from django.core.exceptions import ValidationError
from djongo import models
from django import forms
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from HallOfFame.settings import AUTH_USER_MODEL


# Create your models here.

class DayTime(models.Model):
    day_of_week = models.CharField(max_length=20)
    time = models.TimeField()
    objects = models.DjongoManager()

    def __iter__(self):
        yield 'day_of_week', self.day_of_week
        yield 'time', self.time
    # class Meta:
    #     abstract = True


class DayTimeForm(forms.ModelForm):
    class Meta:
        model = DayTime
        fields = ('day_of_week', 'time')


class Mark(models.Model):
    value = models.IntegerField(default=0.0)
    max_points = models.IntegerField(default=0.0)
    for_what = models.CharField(max_length=100)
    note = models.CharField(max_length=250, blank=True, null=True)
    objects = models.DjongoManager()

    # class Meta:
    #     abstract = True

    def clean(self):
        if self.value > self.max_points:
            raise ValidationError("Student can't get more points than maximal number")


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('value', 'max_points', 'for_what', 'note')


class Inattendence(models.Model):
    class_num = models.IntegerField()
    justified = models.BooleanField(default=False)
    objects = models.DjongoManager()

    # class Meta:
    #     abstract = True


class InattendenceForm(forms.ModelForm):
    class Meta:
        model = Inattendence
        fields = ('class_num', 'justified')


class Enrolled(models.Model):
    student = models.ForeignKey(AUTH_USER_MODEL, models.PROTECT, blank=False, null=False)
    inattendances_list = models.ArrayField(model_container=Inattendence, default=[],blank=False, null=False)
    marks_list = models.ArrayField(model_container=Mark, default=[],blank=False, null=False)
    final_grade = models.FloatField(blank=True, null=True)
    objects = models.DjongoManager()

    # class Meta:
    #     abstract = True


class EnrolledForm(forms.ModelForm):
    class Meta:
        model = Enrolled
        fields = ('student', 'inattendances_list', 'marks_list', 'final_grade')


class Lecture(models.Model):
    lecture = models.ForeignKey(AUTH_USER_MODEL, models.PROTECT, blank=False, null=False)
    main_lecture = models.BooleanField(default=True)
    objects = models.DjongoManager()

    def __iter__(self):
        yield 'lecture_id', self.lecture
        yield 'main_lecture', self.main_lecture
    # class Meta:
    #     abstract = True


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ('lecture', 'main_lecture')


class Group(models.Model):
    course = models.CharField(max_length=120)
    date_time = models.ArrayField(model_container=DayTime, blank=True, null=True)
    lectures_list = models.ArrayField(model_container=Lecture, blank=True, null=True)
    enrolled_list = models.ArrayField(model_container=Enrolled, blank=True, null=True)
    course_end = models.BooleanField(default=False, blank=False)
    objects = models.DjongoManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
