# Generated by Django 2.2.2 on 2019-06-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20190619_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='order_status',
            field=models.CharField(choices=[('DR', '草稿'), ('SM', '已提交'), ('WO', '等待作业'), ('FC', '完成'), ('VO', '作废')], default='SM', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='carton',
            field=models.IntegerField(blank=True, null=True, verbose_name='件数'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='charge_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='计费重量'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='体积'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='重量'),
        ),
    ]
