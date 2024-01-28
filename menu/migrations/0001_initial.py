# Generated by Django 4.2.9 on 2024-01-26 18:01

from django.db import migrations, models
import django.db.models.deletion
import helpers.media_upload


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('prepare_time', models.FloatField(blank=True, null=True)),
                ('calories', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, upload_to=helpers.media_upload.upload_item_images)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='menu.category')),
            ],
        ),
    ]
