# Generated by Django 3.1.7 on 2021-05-01 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0009_auto_20210427_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='end_job',
        ),
        migrations.RemoveField(
            model_name='job',
            name='start_job',
        ),
    ]