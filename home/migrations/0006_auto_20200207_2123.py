# Generated by Django 2.2 on 2020-02-07 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_recommendation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='r_Email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='recommendation',
            old_name='r_Name',
            new_name='Name',
        ),
    ]