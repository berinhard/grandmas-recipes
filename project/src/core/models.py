#coding:utf-8
from django.db import models

class Recipe(models.Model):
    ingredients = models.ManyToManyField("Ingredient", through="IngredientsAmountInRecipe", verbose_name=u"Ingredientes")
    name = models.CharField(verbose_name=u"Nome", max_length=80)
    portions = models.PositiveIntegerField(verbose_name=u"Porções", blank=True, null=True)
    preparation_time = models.PositiveIntegerField(verbose_name="Tempo de preparo (min)", blank=True, null=True)
    preparation_script = models.TextField(verbose_name="Modo de preparo", blank=True, null=True)

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(verbose_name=u"Nome", max_length=50)
    stock_quantity = models.PositiveIntegerField(verbose_name=u"Quantidade no estoque", blank=True, null=True)
    price_per_kilo = models.DecimalField(verbose_name=u"Preço por quilo", max_digits=3, decimal_places=2, blank=True, null=True)
    price_per_unit = models.DecimalField(verbose_name=u"Preço por unidade", max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __unicode__(self):
        return self.name


class IngredientsAmountInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, verbose_name="Ingrediente")
    recipe = models.ForeignKey(Recipe, verbose_name="Receita")
    amount = models.PositiveIntegerField(verbose_name="Quantidade na receita")

    class Meta:
        verbose_name = "Ingrediente da receita"
        verbose_name_plural = "Ingredientes da receita"

    def __unicode__(self):
        return self.amount

