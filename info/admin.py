from django.contrib import admin

# Register your models here.
from info.models import AirportCode, Exchange, Charge


@admin.register(AirportCode)
class AirportCodeAdmin(admin.ModelAdmin):
    list_display = ('airport_code', 'country_code', 'city_code', 'airport_en_name', 'airport_cn_name')
    search_fields = ['airport_code__exact', 'country_code__exact', 'city_code__exact', 'airport_en_name__exact', 'airport_cn_name']



@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('current_currency', 'target_currency', 'multiplying_rate', 'currency_date', 'remark')

    fields = ('current_currency', 'target_currency', 'multiplying_rate', 'currency_date', 'remark')


@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'remark')

    fields = ('name', 'code', 'remark')

    search_fields = ['name']