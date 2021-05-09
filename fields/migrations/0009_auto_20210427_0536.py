# Generated by Django 3.1.7 on 2021-04-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0008_job_jobcategory_worker'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Работа', 'verbose_name_plural': 'Работы'},
        ),
        migrations.AlterField(
            model_name='field',
            name='square_ha',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Площадь поля в гектарах'),
        ),
        migrations.AlterField(
            model_name='job',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='job',
            name='workers',
            field=models.ManyToManyField(related_name='jobs', to='fields.Worker', verbose_name='Исполнители'),
        ),
    ]
