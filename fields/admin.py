from django.contrib import admin
from django.forms import CheckboxSelectMultiple

from fields import models


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'square')
    list_filter = ('name', 'square')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('season', 'field', 'culture')
    list_filter = ('season',)


@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')
    list_filter = ('firstname',)


@admin.register(models.JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_filter = ('category',)


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('category', 'season', 'start_job', 'end_job')
