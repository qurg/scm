from django.db import models

# Create your models here.
from common.models import BaseEntity
from company.models import Customer, Supplier
from info.models import Charge


class MasterOrder(BaseEntity):
    order_num = models.CharField(max_length=30, verbose_name='主单号', null=True)

    class Meta:
        verbose_name_plural = '主单'
        verbose_name = '主单'

    def __str__(self):
        return self.order_num


class HouseOrder(BaseEntity):
    order_num = models.CharField(max_length=30, verbose_name='分单号', null=True)

    class Meta:
        verbose_name_plural = '分单'
        verbose_name = '分单'

    def __str__(self):
        return self.order_num


class CustomerOrder(BaseEntity):
    ORDER_STATUS = [
        ('DR', '草稿'),
        ('SM', '已提交'),
        ('WO', '等待作业'),
        ('FC', '完成'),
        ('VO', '作废'),
    ]

    arrival_date = models.DateField(verbose_name='到货日期')
    order_num = models.CharField(max_length=30, verbose_name='订单号', null=True, blank=True)
    order_status = models.CharField(max_length=30, choices=ORDER_STATUS, null=True, default='SM', verbose_name='订单状态')
    customer = models.ForeignKey(Customer, verbose_name='客户', on_delete=models.DO_NOTHING, null=True)
    pre_carton = models.IntegerField(verbose_name='预计件数')
    pre_weight = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='预计重量')
    pre_volume = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='预计体积')
    pre_size = models.CharField(max_length=500, verbose_name='预报尺寸', null=True, blank=True)
    carton = models.IntegerField(verbose_name='件数', null=True, blank=True)
    weight = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='重量', null=True, blank=True)
    volume = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='体积', null=True, blank=True)
    charge_trans = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='计费转换', null=True, default=6000)
    charge_weight = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='计费重量', null=True, blank=True)
    size = models.CharField(max_length=500, verbose_name='尺寸', null=True, blank=True)
    airline = models.CharField(max_length=20, verbose_name='航空公司')
    airline_date = models.DateField(verbose_name='航班日期')
    master_num = models.ForeignKey(MasterOrder, verbose_name='主单号', null=True, blank=True, on_delete=models.DO_NOTHING)
    house_num = models.ForeignKey(HouseOrder, verbose_name='分单号', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = '客户订单'
        verbose_name = '客户订单'

    def __str__(self):
        return self.order_num


class CustomerOrderChargeOut(BaseEntity):
    CURRENCY = [
        ('CNY', 'CNY'),
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('EUR', 'EUR'),
    ]

    charge_name = models.ForeignKey(Charge, on_delete=models.DO_NOTHING, null=True, verbose_name='费用名称')
    charge_rate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='单价')
    charge_count = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='数量')
    charge_total = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='合计')
    currency_type = models.CharField(max_length=10, choices=CURRENCY, verbose_name='币种', default='CNY')
    current_exchange = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='汇率')
    account_charge = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='记账金额')
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='供应商')
    customer_order_num = models.ForeignKey(CustomerOrder, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return '记录费用 %s 金额 %s %s ' % (self.charge_name, self.charge_total, self.currency_type)


class CustomerOrderChargeIn(BaseEntity):
    CURRENCY = [
        ('CNY', 'CNY'),
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('EUR', 'EUR'),
    ]

    charge_name = models.ForeignKey(Charge, on_delete=models.DO_NOTHING, null=True, verbose_name='费用名称')
    charge_rate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='单价')
    charge_count = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='数量')
    charge_total = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='合计')
    currency_type = models.CharField(max_length=10, choices=CURRENCY, verbose_name='币种', default='CNY')
    current_exchange = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='汇率')
    account_charge = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, verbose_name='记账金额')
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='付款方')
    customer_order_num = models.ForeignKey(CustomerOrder, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return '记录收入 %s 金额 %s %s' % (self.charge_name, self.charge_total, self.currency_type)
