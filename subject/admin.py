from django.contrib import admin

from subject import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('name',)
    list_display_links = list_display


@admin.register(models.Lesson)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('name',)
    list_display_links = list_display
