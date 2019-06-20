from .origin import *

# 线上配置文件

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 线上环境数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'scm',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}
