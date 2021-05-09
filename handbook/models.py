from django.db import models


# class Category(models.Model):
#     name = models.CharField('Имя категории' , max_length=200 , db_index=True)
#     slug = models.SlugField(max_length=200 , unique=True)
#
#     class Meta:
#         ordering = ('name' ,)
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name

from django.urls import reverse


class CategoryCulture(models.Model):
    name = models.CharField('Название культуры', max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип культуры'
        verbose_name_plural = 'Типы культур'

    def __str__(self):
        return self.name


class ChemicalElement(models.Model):
    name = models.CharField('Название элемента', max_length=64, db_index=True)
    abbreviation = models.CharField('Аббревиатура элемента', max_length=12)
    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Химический элемент'
        verbose_name_plural = 'Химические элементы'

    def __str__(self):
        return self.name


class Fertilizer(models.Model):
    """Справочник удобрений"""

    UNIT_CHOICES = [
        ('кг', 'килограмм'),
        ('т', 'тонн'),
        ('г', 'грамм'),
    ]

    COLOR_CHOICES = [
        ('Не окрашенный', 'Нет',),
        ('Окрашенный', 'Да',),
    ]

    name = models.CharField('Название удобрения', max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)
    units = models.CharField(max_length=64, choices=UNIT_CHOICES)
    color = models.CharField(max_length=64, choices=COLOR_CHOICES)
    description = models.TextField()
    advantages = models.TextField()
    culture = models.ManyToManyField(CategoryCulture, verbose_name='Культура',
                                     related_name='fertilizer_cultures')
    compositions = models.ManyToManyField(ChemicalElement , verbose_name='Химический элемент',
                                          related_name='fertilizer_compositions')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Удобрение'
        verbose_name_plural = 'Удобрения'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('handbook:fertilizer_detail', args=[self.slug])


class Pest(models.Model):
    name = models.CharField('Название вредителя', max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)
    image = models.ImageField(upload_to='pests/', blank=True)
    phase = models.CharField('Фаза развития', max_length=128)
    organ = models.CharField('Поражаемые органы', max_length=128)
    description = models.TextField()
    region = models.TextField('Регион распространения')
    culture = models.ManyToManyField(CategoryCulture, verbose_name='Культура',
                                     related_name='pest_cultures')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Вредитель'
        verbose_name_plural = 'Вредители'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('handbook:pest_detail', args=[self.slug])
