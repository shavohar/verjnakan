# Generated by Django 5.0.1 on 2024-01-28 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_contactus_follow_us_links_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='follow_us_links',
            new_name='follow_us',
        ),
    ]