from django.contrib import admin


class ScmAdminSite(admin.AdminSite):
    site_header = '伍星供应链'
    site_title = site_header
    index_title = '功能列表'
