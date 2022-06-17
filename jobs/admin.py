from django.contrib import admin
from .models import Jobs

# Register your models here.
admin.site.register(Jobs)

"""
    管理画面タイトル変更
"""
admin.site.site_header = 'コンテンツ管理'