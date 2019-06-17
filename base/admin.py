import time

from django.contrib.admin import ModelAdmin


class BaseAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.create_by is None:
            obj.create_by = request.user
            obj.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if change:
            obj.update_by = request.user
            obj.update_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return super(BaseAdmin, self).save_model(request, obj, form, change)
