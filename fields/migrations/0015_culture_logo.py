# Generated by Django 3.1.7 on 2021-05-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0014_remove_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='culture',
            name='logo',
            field=models.ImageField(default=231, upload_to='cultures'),
            preserve_default=False,
        ),
    ]
