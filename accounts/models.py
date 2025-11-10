from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, number, password, **extra_fields):
        number = number
        if not number or len(number) != 11 or not number.startswith('09'):
            raise ValueError('Please enter a right number')

        user = self.create(number=number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(number, password, **extra_fields)


class User(AbstractUser):
    bio      = models.TextField(max_length=500, blank=True, null=True)
    picture  = models.ImageField(upload_to='account/user_pictures', default='account/user_pictures/default.jpg')
    number   = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD  = 'number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.username}-{self.number}'


class LinkUser(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links_user')
    telegram  = models.URLField(max_length=100, blank=True, null=True)
    x         = models.URLField(max_length=100, blank=True, null=True)
    instagram = models.URLField(max_length=100, blank=True, null=True)
    github    = models.URLField(max_length=100, blank=True, null=True)
    facebook  = models.URLField(max_length=100, blank=True, null=True)
    youtube   = models.URLField(max_length=100, blank=True, null=True)
    linkedin  = models.URLField(max_length=100, blank=True, null=True)