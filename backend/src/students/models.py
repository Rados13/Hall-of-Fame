from djongo import models
from django.urls import reverse


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    pasword = models.CharField(max_length=120)

    objects = models.DjongoManager()

    def get_absolute_url(self):
        return reverse("students:view", kwargs={"id": self.id})
        # return f"/students/{self.id}"
