from djongo import models
from django import forms


class Mark(models.Model):
    value = models.IntegerField(default=0.0)
    max_points = models.IntegerField(default=0.0)
    for_what = models.CharField(max_length=100)
    note = models.CharField(max_length=250, blank=True, null=True)
    objects = models.DjongoManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # class Meta:
    #     abstract = True

    # def clean(self):
    #     if self.value > self.max_points:
    #         raise ValidationError("Student can't get more points than maximal number")


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('value', 'max_points', 'for_what', 'note')
