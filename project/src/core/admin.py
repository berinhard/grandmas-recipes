#coding:utf-8
from django.contrib import admin
from src.core.models import Recipe, Ingredient, IngredientsAmountInRecipe
from src.core.forms import RequiredInlineFormSet


class IngredientsAmountInRecipeInline(admin.TabularInline):
    model = IngredientsAmountInRecipe
    extra = 1
    formset = RequiredInlineFormSet

class RecipeAdmin(admin.ModelAdmin):

    list_display = ['name', 'portions', 'preparation_time']
    search_fields = ['name', 'preparation_script']
    inlines = (IngredientsAmountInRecipeInline,)
    exclude = ('ingredients',)

class IngredientAdmin(admin.ModelAdmin):

    list_display = ['name', 'stock_quantity', 'price_per_kilo', 'price_per_unit']
    search_fields = ['name']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
