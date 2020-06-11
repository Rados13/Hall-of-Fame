from djongo import models
from django import forms


class DayTime(models.Model):
    day_of_week = models.CharField(max_length=20)
    time = models.TimeField()
    objects = models.DjongoManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        yield 'day_of_week', self.day_of_week
        yield 'time', self.time
    # class Meta:
    #     abstract = True


class DayTimeForm(forms.ModelForm):
    class Meta:
        model = DayTime
        fields = ('day_of_week', 'time')
