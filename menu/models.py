from django.db import models
from django.urls import reverse

from helpers.media_upload import upload_item_images


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    prepare_time = models.FloatField(null=True, blank=True)
    calories = models.FloatField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to=upload_item_images, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="item")

    def __str__(self):
        return self.name
