from django.db import models
from base.models import BaseEntity


# Create your models here.
class Company(BaseEntity):
    name = models.CharField(max_length=300, verbose_name='公司名称')
    short_name = models.CharField(max_length=100, verbose_name='公司简称')

    class Meta:
        abstract = True


class Customer(Company):
    class Meta:
        verbose_name = '客户管理'
        verbose_name_plural = '客户管理'

    def __str__(self):
        return self.name


class Supplier(Company):
    class Meta:
        verbose_name = '供应商管理'
        verbose_name_plural = '供应商管理'

    def __str__(self):
        return self.name
