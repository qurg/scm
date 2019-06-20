from datetime import *

from django.contrib import admin

# Register your models here.
from django.db.models import Sum

from common.admin import BaseAdmin
from info.models import Exchange
from order.adminForms import CustomerOrderAdminForm
from order.models import MasterOrder, HouseOrder, CustomerOrder, CustomerOrderChargeOut, CustomerOrderChargeIn


class CustomerOrderChargeOutAdmin(admin.TabularInline):
    model = CustomerOrderChargeOut
    extra = 0
    fields = ('charge_name', 'charge_rate', 'charge_count', 'charge_total', 'currency_type', 'supplier')

    autocomplete_fields = ['charge_name', 'supplier', ]
    readonly_fields = ['charge_total', ]
    verbose_name = '成本项'
    verbose_name_plural = '成本明细'


class CustomerOrderChargeInAdmin(admin.TabularInline):
    model = CustomerOrderChargeIn
    extra = 0
    fields = ('charge_name', 'charge_rate', 'charge_count', 'charge_total', 'currency_type', 'customer')

    autocomplete_fields = ['charge_name', 'customer', ]
    readonly_fields = ['charge_total', ]
    verbose_name = '收入项'
    verbose_name_plural = '收入明细'


@admin.register(CustomerOrder)
class CustomerOrderAdmin(BaseAdmin):
    form = CustomerOrderAdminForm

    list_display = ('order_num', 'order_status', 'customer', 'airline', 'airline_date',
                    'pre_carton', 'pre_weight', 'pre_volume', 'carton', 'weight', 'volume',
                    'master_num', 'house_num', 'total_charge_in', 'total_charge_out')

    fieldsets = (
        (None, {
            'fields': (
                ('order_num', ),
                ('customer','order_status', ),
                ('airline', 'airline_date', ),
                ('master_num', 'house_num',),
            )
        }),
        ('货物信息', {
            'fields': (
                ('pre_carton', 'pre_weight', 'pre_volume',),
                ('carton', 'weight', 'volume',),
                ('charge_trans', 'charge_weight',),
                ('pre_size', 'size',),
            )
        }),
    )

    # # 显示过滤条件
    # list_filter = ('airline_date', 'customer',)

    search_fields = ['customer__name', 'order_num', ]

    # 列表业会显示当前日期
    date_hierarchy = 'arrival_date'

    # # 拼合字段使用
    # prepopulated_fields = {'size': ('airline', 'airline_date')}

    autocomplete_fields = ['customer', 'master_num', 'house_num', ]

    # # 显示外键字段信息
    # raw_id_fields = ['master_num']

    readonly_fields = ['order_num', 'charge_weight']

    inlines = [CustomerOrderChargeInAdmin, CustomerOrderChargeOutAdmin, ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.order_num is None:
            id_num = str(obj.id)
            obj.order_num = 'F' + id_num.zfill(5)
        return super(CustomerOrderAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        # 将多币种转换
        for instance in instances:
            # 获取当天的汇率，如果获取不成功就拿最新的汇率
            try:
                exchange = Exchange.objects.get(currency_date=date.today(), current_currency=instance.currency_type)
            except Exchange.DoesNotExist:
                exchange = Exchange.objects.filter(current_currency=instance.currency_type).latest('currency_date')

            instance.current_exchange = exchange.multiplying_rate

            if instance.charge_rate is not None and instance.charge_count is not None:
                instance.charge_total = instance.charge_rate * instance.charge_count
                instance.account_charge = instance.charge_total * exchange.multiplying_rate

            if formset.model == CustomerOrderChargeIn and instance.customer is None:
                instance.customer = form.instance.customer
            instance.save()
        # 保存数据
        formset.save_m2m()
        return super(CustomerOrderAdmin, self).save_formset(request, form, formset, change)

    def total_charge_in(self, obj):
        return CustomerOrderChargeIn.objects.filter(customer_order_num=obj.id).aggregate(
            total=Sum('account_charge'))['total']

    total_charge_in.short_description = '总收入'

    def total_charge_out(self, obj):
        return CustomerOrderChargeOut.objects.filter(customer_order_num=obj.id).aggregate(
            total=Sum('account_charge'))['total']

    total_charge_out.short_description = '总支出'


@admin.register(MasterOrder)
class MasterOrderAdmin(BaseAdmin):
    search_fields = ['order_num', ]


@admin.register(HouseOrder)
class HouseOrderAdmin(BaseAdmin):
    search_fields = ['order_num']
