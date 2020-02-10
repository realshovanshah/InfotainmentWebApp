# Generated by Django 2.2 on 2020-02-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=40)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=20)),
                ('user_description', models.TextField()),
            ],
        ),
    ]
