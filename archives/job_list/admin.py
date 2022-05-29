from django.contrib import admin
from .models import JobModel

# Register your models here.
admin.site.register(JobModel)

"""
    管理画面タイトル変更
"""
admin.site.site_header = 'コンテンツ管理'

# Site administration を変更
# admin.site.index_title = 'テキスト'
