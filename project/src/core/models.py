#coding:utf-8
from django.db import models

class Recipe(models.Model):
    ingredients = models.ManyToManyField("Ingredient", related_name="recipes_ingredients", verbose_name=u"Ingredientes")
    name = models.CharField(verbose_name=u"Nome", max_length=80)
    portions = models.PositiveIntegerField(verbose_name=u"Porções", blank=True, null=True)
    preparation_time = models.PositiveIntegerField(verbose_name="Tempo de preparo (min)", blank=True, null=True)
    preparation_script = models.TextField(verbose_name="Modo de preparo", blank=True, null=True)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(verbose_name=u"Nome", max_length=50)
    recipe = models.ManyToManyField("Recipe", blank=True, null=True, verbose_name=u"Receitas")
    stock_quantity = models.PositiveIntegerField(verbose_name=u"Quantidade no estoque", blank=True, null=True)
    price_per_kilo = models.DecimalField(verbose_name=u"Preço por quilo", max_digits=3, decimal_places=2, blank=True, null=True)
    price_per_unit = models.DecimalField(verbose_name=u"Preço por unidade", max_digits=3, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return self.name


class IngredientsAmountInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    amount = models.PositiveIntegerField(verbose_name="Quantidade na receita")

    def __unicode__(self):
        return self.amount
