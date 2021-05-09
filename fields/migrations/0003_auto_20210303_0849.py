# Generated by Django 3.1.7 on 2021-03-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0002_auto_20210303_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='actual_harvest',
            field=models.IntegerField(blank=True, null=True, verbose_name='Фактический урожай'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='density',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Плотность засева'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='harvest_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата сбора'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='planned_harvest',
            field=models.IntegerField(blank=True, null=True, verbose_name='Планируемый урожай'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='sowing_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата сева'),
        ),
    ]
