from django.contrib.admin.apps import AdminConfig


class ScmAdminConfig(AdminConfig):
    default_site = 'scm.admin.ScmAdminSite'
