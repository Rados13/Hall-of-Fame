from djongo import models
from dayTime.models import DayTime
from enrolleds.models import Enrolled
from lectures.models import Lecture


class Group(models.Model):
    course = models.CharField(max_length=120)
    date_time = models.ArrayField(model_container=DayTime, blank=True, null=True)
    lectures_list = models.ArrayField(model_container=Lecture, blank=True, null=True)
    enrolled_list = models.ArrayField(model_container=Enrolled, blank=True, null=True)
    course_end = models.BooleanField(default=False, blank=False)
    objects = models.DjongoManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
