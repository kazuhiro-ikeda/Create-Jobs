from django.db import models
import uuid


# Create your models here.
class JobModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    title = models.CharField(verbose_name='タイトル[必須]', max_length=256)
    date = models.DateField(verbose_name='掲載開始日[必須]')
    company = models.CharField(verbose_name='企業名[必須]', max_length=256, default='株式会社ABCDE')
    country = models.CharField(verbose_name='国名[必須]', max_length=10, default='日本')
    postalcode = models.CharField(verbose_name='郵便番号[必須]', max_length=10, default='166-0002')
    state = models.CharField(verbose_name='都道府県[必須]', max_length=10, default='東京都')
    city = models.CharField(verbose_name='市区町村[必須]', max_length=10, default='杉並区')
    rawlocation = models.CharField(verbose_name='番地など', max_length=256, null=True, blank=True, default='高円寺')
    streetaddress = models.CharField(verbose_name='勤務地', max_length=256, default='東京都杉並区高円寺１丁目１−１−１')
    email = models.EmailField(verbose_name='応募先メール', max_length=256, null=True, blank=True,)
    station = models.TextField(verbose_name='最寄駅', max_length=50, null=True, blank=True, default='JR高円寺')
    subwayaccess = models.TextField(verbose_name='交通アクセス', null=True, blank=True, max_length=256)
    category = models.CharField(verbose_name='職種[カンマ区切り]', max_length=256, null=True, blank=True, default='Pythonエンジニア')
    jobtype = models.CharField(verbose_name='雇用形態', max_length=256, null=True, blank=True, default='正社員')
    description = models.TextField(verbose_name='職務内容[必須]', max_length=1000, default='<h2>◆仕事内容</h2>')
    salary = models.TextField(verbose_name='給与概略[必須]', max_length=256, default='250,000円〜')
    rawsalary = models.TextField(verbose_name='給与詳細', max_length=256, null=True, blank=True)
    timeshift = models.TextField(verbose_name='勤務時間', max_length=256, null=True, blank=True)
    education = models.TextField(verbose_name='最終学歴', max_length=256, null=True, blank=True, default='四年生大学卒業')
    experience = models.TextField(verbose_name='経験', max_length=256, null=True, blank=True, default='5年以上')
    benefits = models.TextField(verbose_name='待遇・福利厚生', max_length=256, null=True, blank=True)
    expirationdate = models.DateField(verbose_name='掲載期限', null=True, blank=True)
    expdate = models.DateField(verbose_name='最終掲載日', null=True, blank=True)
    tracking_url = models.CharField(verbose_name='追跡タグ', max_length=256, null=True, blank=True)
    imageUrls = models.CharField(verbose_name='画像URL', max_length=500, null=True, blank=True)
    hires = models.CharField(verbose_name='採用予定人数', max_length=256, null=True, blank=True)
    keywords = models.CharField(verbose_name='キーワード[カンマ区切り]', max_length=256, null=True, blank=True)
