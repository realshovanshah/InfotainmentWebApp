# Generated by Django 2.2 on 2020-02-10 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('shows_id', models.AutoField(primary_key=True, serialize=False)),
                ('shows_Name', models.CharField(max_length=50)),
                ('shows_Description', models.TextField()),
                ('shows_Type', models.CharField(choices=[('TV Show', 'TV Show'), ('Movie', 'Movie')], max_length=20)),
                ('shows_Genre', models.CharField(choices=[('Sci-Fi', 'Sci-Fi'), ('Drama', 'Drama'), ('Romance', 'Romance'), ('Comedy', 'Comedy'), ('Fantasy', 'Fantasy'), ('Thriller', 'Thriller')], max_length=20)),
                ('shows_Image', models.FileField(upload_to='shows/')),
                ('is_favorite', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shows', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Show')),
            ],
        ),
    ]
