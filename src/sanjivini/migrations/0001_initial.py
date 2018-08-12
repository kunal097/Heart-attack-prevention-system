# Generated by Django 2.0.7 on 2018-07-26 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=15, unique=True)),
                ('device_secret', models.CharField(max_length=16, unique=True)),
            ],
        ),
    ]
