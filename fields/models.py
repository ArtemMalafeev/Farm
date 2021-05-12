from dateutil.relativedelta import relativedelta
import datetime
from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Season(models.Model):
    name = models.CharField(max_length=4, unique=True)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class Culture(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    logo = models.ImageField(upload_to='cultures')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Культура'
        verbose_name_plural = 'Культуры'


class Field(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_fields')
    name = models.CharField("Название поля", max_length=64, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    square = models.PositiveIntegerField('Площадь поля в квадратных метрах')
    square_ha = models.DecimalField('Площадь поля в гектарах', max_digits=10, decimal_places=3)
    coordinate = models.TextField()
    cadastral_number = models.CharField('Кадастровый номер', max_length=64)

    def __str__(self):
        return '{0} - {1}га'.format(self.name, self.square)

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'

    def get_coordinate_field(self):
        result = self.coordinate.split(',')[:2]

        return ', '.join(result)

    def get_absolute_url(self):
        return reverse('fields:field_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        """Определяем автоматический slug, для несуществующих объектов."""
        if not self.id:
            self.slug = slugify(self.name)

        super(Field, self).save(*args, **kwargs)


class Crop(models.Model):
    season = models.ForeignKey(Season, related_name='crops', on_delete=models.CASCADE)
    field = models.ForeignKey(Field,  related_name='crops', on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, related_name='crops', on_delete=models.CASCADE)
    planned_harvest = models.IntegerField('Планируемый урожай', blank=True, null=True)
    actual_harvest = models.IntegerField('Фактический урожай', blank=True, null=True)
    sowing_date = models.DateField('Дата сева', blank=True, null=True)
    harvest_date = models.DateField('Дата сбора', blank=True, null=True)
    density = models.CharField('Плотность засева', max_length=32, blank=True, null=True)

    def __str__(self):
        return self.season.name

    class Meta:
        verbose_name = 'Сев'
        verbose_name_plural = 'Севы'


class Worker(models.Model):
    """ Исполнители """
    firstname = models.CharField(max_length=32, verbose_name='Имя')
    lastname = models.CharField(max_length=32, verbose_name='Фамилия')

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        unique_together = ('firstname', 'lastname')


class JobCategory(models.Model):
    """ Наименование работ """
    category = models.CharField(max_length=128, verbose_name='Наименование работы')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Наименование работы'
        verbose_name_plural = 'Наименование работ'


class Job(models.Model):
    """ Работы """
    category = models.ForeignKey(JobCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='Наименование работы')
    season = models.ForeignKey(Season,
                               on_delete=models.CASCADE,
                               verbose_name='Сезон')
    start_job = models.DateTimeField(verbose_name='Начало работы')
    end_job = models.DateTimeField(verbose_name='Конец работы')
    fields = models.ManyToManyField(Field, related_name='jobs', verbose_name='Список полей')
    workers = models.ManyToManyField(Worker, verbose_name='Исполнители', related_name='jobs')
    comment = models.TextField(verbose_name='Комментарии', blank=True)

    def get_process_job(self):
        now = timezone.now()

        if now <= self.start_job:
            return 0

        total_duration = self.end_job - self.start_job
        process = now - self.start_job
        left = total_duration - process

        result = round((process / total_duration) * 100)

        if result > 100:
            return 100
        else:
            return result

    def get_status_job(self):
        status = ('Ожидается', 'Выполняется', 'Выполнено')
        now = timezone.now()

        if now < self.start_job:
            return status[0]

        if (now >= self.start_job) and (now <= self.end_job):
            return status[1]

        if now > self.end_job:
            return status[2]

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
