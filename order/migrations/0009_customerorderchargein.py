# Generated by Django 2.2.2 on 2019-06-19 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_charge'),
        ('company', '0007_airline'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0008_auto_20190619_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrderChargeIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('del_flag', models.BooleanField(default=False, editable=False, verbose_name='删除')),
                ('charge_rate', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='单价')),
                ('charge_count', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='数量')),
                ('charge_total', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='合计')),
                ('currency_type', models.CharField(choices=[('CNY', 'CNY'), ('USD', 'USD'), ('GBP', 'GBP'), ('EUR', 'EUR')], default='CNY', max_length=10, verbose_name='币种')),
                ('current_exchange', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='汇率')),
                ('account_charge', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='记账金额')),
                ('charge_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='info.Charge', verbose_name='费用名称')),
                ('create_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.Customer', verbose_name='付款方')),
                ('customer_order_num', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='order.CustomerOrder')),
                ('update_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update+', to=settings.AUTH_USER_MODEL, verbose_name='更新人')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
