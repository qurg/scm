from django.contrib import admin
from django.core.mail import send_mail

# Register your models here.
from django.contrib.admin import ModelAdmin

from common.admin import BaseAdmin
from company.models import Customer, Supplier, Airline


# 定义批量操作
def sendmail_customer(customerAdmin, request, queryset):
    send_mail(
        'Subject here',
        'Here is the message.',
        '',
        ['rengang.qu@icloud.com'],
        fail_silently=False,
    )


sendmail_customer.short_description = 'Sent email to customer'


@admin.register(Customer)
class CustomerAdmin(BaseAdmin):
    fields = ('name', 'short_name', 'remark')

    list_display = ('id', 'short_name', 'name', 'remark')

    search_fields = ['name']

    actions = [sendmail_customer]


@admin.register(Airline)
class AirlineAdmin(BaseAdmin):
    list_display = ('name', 'short_name', 'code', 'prefix', 'web')

    fields = ('name', 'short_name', 'code', 'prefix', 'web')


@admin.register(Supplier)
class SupplierAdmin(BaseAdmin):
    fields = ('name', 'short_name', 'remark')

    list_display = ('id', 'short_name', 'name', 'remark')

    search_fields = ['name']
