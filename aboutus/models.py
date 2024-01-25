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
