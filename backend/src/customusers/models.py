from djongo import models
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth import get_user_model


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


# Create your models here.
class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
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
