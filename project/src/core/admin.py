#coding:utf-8
from django.contrib import admin
from src.core.models import Recipe

class RecipeAdmin(admin.ModelAdmin):

    list_display = ['name', 'portions', 'preparation_time']
    search_fields = ['name', 'preparation_script']

admin.site.register(Recipe, RecipeAdmin)
