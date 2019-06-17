from django.apps import apps
from django.contrib import admin
from django.utils.text import capfirst


class ScmAdminSite(admin.AdminSite):
    site_header = '伍星供应链'
    site_title = site_header
    index_title = '功能列表'


def find_app_index(app_label):
    app = apps.get_app_config(app_label)
    main_menu_index = getattr(app, 'main_menu_index', 9999)
    return main_menu_index


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        app_list = templateresponse.context_data['app_list']
        app_list.sort(key=lambda r: find_app_index(r['app_label']))
        for app in app_list:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse

    return inner


# registry = OrderedDict()
# registry.update(admin.site._registry)
# admin.site._registry = registry
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
