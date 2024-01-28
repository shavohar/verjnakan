from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from helpers.media_upload import upload_user_images


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValidationError("email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=155, blank=True, null=True)
    last_name = models.CharField(max_length=155, blank=True, null=True)
    image = models.ImageField(upload_to=upload_user_images)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = "email"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_user_images, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_field = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


@receiver(post_save, sender=User)
def profile_post_save(instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
