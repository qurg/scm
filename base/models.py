from django.conf import settings
from django.db import models


# Create your models here.
class BaseEntity(models.Model):
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, verbose_name='创建人',
                                  editable=False)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', editable=False)
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, verbose_name='更新人',
                                  related_name='update+', editable=False)
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='更新时间', editable=False)
    remark = models.CharField(max_length=500, verbose_name='备注', null=True, blank=True)
    del_flag = models.BooleanField(default=False, verbose_name='删除', editable=False)

    class Meta:
        abstract = True
