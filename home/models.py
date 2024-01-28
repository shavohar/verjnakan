from django.db import models
from helpers.media_upload import upload_about_us, upload_chef, upload_why_choose_us


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_about_us)

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_why_choose_us)

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to=upload_chef)

    def __str__(self):
        return self.name


class FollowUs(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.name}"


class ContactUs(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    opening_hours = models.CharField(max_length=100)
    follow_us = models.ManyToManyField(FollowUs, blank=True, related_name="contact_us")

    def __str__(self):
        return f"Contact Information: {self.address}, {self.phone_number}, {self.email}, {self.opening_hours}"
