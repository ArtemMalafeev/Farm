# Generated by Django 3.1.7 on 2021-05-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0012_auto_20210509_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='square_ha',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Площадь поля в гектарах'),
        ),
    ]