from djongo import models
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.utils import timezone
from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):
    def create_user(self, email, password=None,**kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


    def get_absolute_url(self):
        return reverse("users:view", kwargs={"pk": self.pk})
        # return f"/users/{self.id}"

    def get_full_name(self):
        return self.first_name.__str__()+"  "+self.last_name.__str__()

    def get_api_uri(self, request=None):
        return api_reverse('api-users:student-rud', kwargs={'pk': self.pk}, request=request)

