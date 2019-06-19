# Generated by Django 2.2.2 on 2019-06-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190619_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='charge_trans',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='计费转换'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='charge_weight',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='计费重量'),
        ),
    ]
