from django.db import models

# Create your models here.
from common.models import BaseEntity


class AirportCode(BaseEntity):
    airport_code = models.CharField(max_length=10, verbose_name='三字代码')
    country_code = models.CharField(max_length=10, verbose_name='国家代码')
    city_code = models.CharField(max_length=10, verbose_name='城市代码')
    airport_en_name = models.CharField(max_length=100, verbose_name='机场英文')
    airport_cn_name = models.CharField(max_length=100, verbose_name='机场中文')

    class Meta:
        verbose_name_plural = '三字代码'
        verbose_name = '三字代码'

    def __str__(self):
        return self.airport_code


class Exchange(BaseEntity):
    current_currency = models.CharField(max_length=10, verbose_name='当前币种')
    target_currency = models.CharField(max_length=10, verbose_name='目标币种')
    multiplying_rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='转换率')
    currency_date = models.DateField(verbose_name='汇率日期')

    class Meta:
        verbose_name = '汇率管理'
        verbose_name_plural = '汇率管理'

    def __str__(self):
        return self.current_currency


class Charge(BaseEntity):
    code = models.CharField(max_length=100, verbose_name='费用代码')
    name = models.CharField(max_length=300, verbose_name='费用名称')

    class Meta:
        verbose_name = '费用代码管理'
        verbose_name_plural = '费用代码管理'

    def __str__(self):
        return self.name
