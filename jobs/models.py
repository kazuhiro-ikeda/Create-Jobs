from django.db import models
import uuid

class Jobs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=100)
    company = models.CharField(verbose_name='会社名', max_length=100, default='合同会社マーリー')

    def __str__(self):
        return self.title