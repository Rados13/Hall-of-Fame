from djongo import models
from django import forms
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

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
    value = models.IntegerField()
    for_what = models.CharField(max_length=100)
    note = models.CharField(max_length=250, blank=True, null=True)
    objects = models.DjongoManager()

    # class Meta:
    #     abstract = True


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('value', 'for_what', 'note')


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
    user_id = models.IntegerField()
    inattendances_list = models.ArrayField(model_container=Inattendence, blank=True, null=True)
    marks_list = models.ArrayField(model_container=Mark, blank=True, null=True)
    objects = models.DjongoManager()

    # class Meta:
    #     abstract = True


class EnrolledForm(forms.ModelForm):
    class Meta:
        model = Enrolled
        fields = ('user_id', 'inattendances_list', 'marks_list')


class Lecture(models.Model):
    lecture_id = models.IntegerField()
    main_lecture = models.BooleanField(default=True)
    objects = models.DjongoManager()

    def __iter__(self):
        yield 'lecture_id', self.lecture_id
        yield 'main_lecture', self.main_lecture
    # class Meta:
    #     abstract = True


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ('lecture_id', 'main_lecture')


class Group(models.Model):
    course = models.CharField(max_length=120)
    date_time = models.ArrayField(model_container=DayTime, blank=True, null=True)
    lectures_list = models.ArrayField(model_container=Lecture, blank=True, null=True)
    enrolled_list = models.ArrayField(model_container=Enrolled, blank=True, null=True)
    objects = models.DjongoManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


