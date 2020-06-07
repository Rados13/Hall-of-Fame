from djongo import models
from django import forms


class Inattendance(models.Model):
    class_num = models.IntegerField()
    justified = models.BooleanField(default=False)
    objects = models.DjongoManager()

    # class Meta:
    #     abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InattendanceForm(forms.ModelForm):
    class Meta:
        model = Inattendance
        fields = ('class_num', 'justified')
