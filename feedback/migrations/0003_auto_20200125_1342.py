# Generated by Django 3.0.2 on 2020-01-25 07:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0002_auto_20200125_1338'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Comment',
        ),
    ]