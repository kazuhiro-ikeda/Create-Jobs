from django.contrib import admin
from .models import Jobs, Jobtype

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Jobtype)


"""
    管理画面タイトル変更
"""
admin.site.site_header = 'コンテンツ管理'