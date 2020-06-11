from HallOfFame.settings import AUTH_USER_MODEL
from djongo import models
from django import forms


class Lecture(models.Model):
    lecture = models.ForeignKey(AUTH_USER_MODEL, models.PROTECT, blank=False, null=False)
    main_lecture = models.BooleanField(default=True)
    objects = models.DjongoManager()

    # def __iter__(self):
    #     yield 'lecture_id', self.lecture
    #     yield 'main_lecture', self.main_lecture
    # class Meta:
    #     abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ('lecture', 'main_lecture')
