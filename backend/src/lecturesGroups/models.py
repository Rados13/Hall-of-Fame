from djongo import models
from HallOfFame.settings import AUTH_USER_MODEL
from groups.models import Group


class LectureGroups(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, models.PROTECT, blank=False, null=False)
    groups_list = models.ArrayReferenceField(to=Group, on_delete=models.PROTECT, blank=True, null=True)
    objects = models.DjongoManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
