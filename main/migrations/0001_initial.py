
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
