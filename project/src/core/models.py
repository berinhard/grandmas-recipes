#coding:utf-8
from django.db import models

class Recipe(models.Model):
    name = models.CharField(verbose_name=u"Nome", max_length=80)
    portions = models.PositiveIntegerField(verbose_name=u"Porções", blank=True, null=True)
    preparation_time = models.PositiveIntegerField(verbose_name="Tempo de preparo (min)", blank=True, null=True)
    preparation_script = models.TextField(verbose_name="Modo de preparo", blank=True, null=True)

    def __unicode__(self):
        return self.name
