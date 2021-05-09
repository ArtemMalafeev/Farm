from django.contrib import admin

from handbook.models import CategoryCulture , ChemicalElement , Fertilizer , Pest


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}


@admin.register(Fertilizer)
class FertilizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'created', 'updated', 'post')
    list_filter = ('post', 'created', 'updated')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CategoryCulture)
class CategoryCultureAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ChemicalElement)
class ChemicalElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Pest)
class ChemicalElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
