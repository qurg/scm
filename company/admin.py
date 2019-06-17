from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from base.admin import BaseAdmin
from company.models import Customer, Supplier


@admin.register(Customer)
class CustomerAdmin(BaseAdmin):
    fields = ('name', 'short_name', 'remark')

    list_display = ('id', 'short_name', 'name', 'remark')


@admin.register(Supplier)
class SupplierAdmin(BaseAdmin):
    fields = ('name', 'short_name', 'remark')

    list_display = ('id', 'short_name', 'name', 'remark')