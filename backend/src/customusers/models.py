from djongo import models
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse


# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    objects = models.DjongoManager()

    def get_absolute_url(self):
        return reverse("customusers:view", kwargs={"pk": self.pk})
        # return f"/customusers/{self.id}"

    # For permissions
    # @property
    # def owner(self):
    #     return self.user

    def get_api_uri(self, request=None):
        return api_reverse('api-customusers:student-rud', kwargs={'pk': self.pk}, request=request)
