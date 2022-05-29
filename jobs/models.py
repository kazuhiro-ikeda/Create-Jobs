from django.db import models
import uuid
import datetime


class Jobs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル[必須]', max_length=100)
    publish = models.DateField(verbose_name='公開日[必須]', null=True, blank=True)
    validthrough = models.DateField(verbose_name='公開終了日[必須]', null=True, blank=True)
    company = models.CharField(verbose_name='会社名[必須]', max_length=100, default='合同会社マーリー')
    country = models.CharField(verbose_name='国名[必須]', max_length=10, default='JP')

    def __str__(self):
        return self.title
