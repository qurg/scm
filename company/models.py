from django.db import models
from base.models import BaseEntity


# Create your models here.
class Company(BaseEntity):
    name = models.CharField(max_length=300, verbose_name='公司名称')
    short_name = models.CharField(max_length=100, verbose_name='公司简称')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Customer(Company):
    class Meta:
        verbose_name = '客户管理'
        verbose_name_plural = '客户管理'


class Airline(Company):
    code = models.CharField(max_length=10, verbose_name='二字代码')
    prefix = models.CharField(max_length=10, verbose_name='前缀')
    web = models.URLField(max_length=300, verbose_name='网址')

    class Meta:
        verbose_name = '航空公司'
        verbose_name_plural = '航空公司'


class Supplier(Company):
    class Meta:
        verbose_name = '供应商管理'
        verbose_name_plural = '供应商管理'
