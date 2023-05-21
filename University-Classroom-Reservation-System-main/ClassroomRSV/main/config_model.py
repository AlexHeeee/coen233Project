# coding:utf-8

from django.db import models

from .model import BaseModel


class config(BaseModel):
    name = models.CharField(max_length=100, verbose_name=u'key')
    value = models.CharField(max_length=100, verbose_name=u'value')

    __tablename__ = 'config'

    class Meta:
        db_table = 'config'
        verbose_name = verbose_name_plural = u'table'