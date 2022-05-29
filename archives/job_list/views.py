import urllib.parse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView, FormView
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import StreamingHttpResponse
from django import forms
from .models import JobModel
from .forms import JobModelForm, CSVUploadForm
import csv
import io


def login_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('admin_navi')
        else:
            return render(request, 'login.html', {'error': 'User Name と Password をご確認ください。'})
    return render(request, 'login.html')


@login_required()  # settings.LOGIN_URL にリダイレクト
def admin_navi_func(request):
    template_name = 'admin_navi.html'
    return render(request, 'admin_navi.html')


def logout_func(request):
    logout(request)
    return redirect('login')


def list_func(request):
    object_list = JobModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def job_func(request, pk):
    object = get_object_or_404(JobModel, pk=pk)
    return render(request, 'job.html', {'object': object})


def job_admin_func(request, pk):
    object = get_object_or_404(JobModel, pk=pk)
    return render(request, 'job_admin.html', {'object': object})


class JobUpdate(UpdateView):
    template_name = 'update.html'
    model = JobModel
    form_class = JobModelForm

    def get_success_url(self):
        return reverse('job', kwargs={"pk": self.object.pk})


class JobDlete(DeleteView):
    template_name = 'delete.html'
    model = JobModel
    success_url = reverse_lazy('list')


class JobCreate(CreateView):
    template_name = 'create.html'
    model = JobModel
    form_class = JobModelForm

    def get_success_url(self):
        return reverse('job', kwargs={"pk": self.object.pk})


def jobs_export(request):
    response = HttpResponse(content_type='text/csv;')
    filename = urllib.parse.quote((u'jobs.csv'))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    fieldnames = [
        'ID[編集不可]',
        'タイトル[必須]',
        '掲載開始日[必須]',
        '企業名[必須]',
        '国名[必須]',
        '郵便番号[必須]',
        '都道府県[必須]',
        '市区町村[必須]',
        '番地など',
        '勤務地',
        '応募先メール',
        '最寄駅',
        '交通アクセス',
        '職種[カンマ区切り]',
        '雇用形態',
        '職務内容[必須]',
        '給与概略[必須]',
        '給与詳細',
        '勤務時間',
        '最終学歴',
        '経験',
        '待遇・福利厚生',
        '掲載期限',
        '最終掲載日',
        '追跡タグ',
        '画像URL',
        '採用予定人数',
        'キーワード[カンマ区切り]',
        '作成日時[自動入力]'
    ]
    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()
    for object in JobModel.objects.all():
        writer.writerow(
            {
                'ID[編集不可]': object.id,
                'タイトル[必須]': object.title,
                '掲載開始日[必須]': object.date,
                '企業名[必須]': object.company,
                '国名[必須]': object.country,
                '郵便番号[必須]': object.postalcode,
                '都道府県[必須]': object.state,
                '市区町村[必須]': object.city,
                '番地など': object.rawlocation,
                '勤務地': object.streetaddress,
                '応募先メール': object.email,
                '最寄駅': object.station,
                '交通アクセス': object.subwayaccess,
                '職種[カンマ区切り]': object.category,
                '雇用形態': object.jobtype,
                '職務内容[必須]': object.description,
                '給与概略[必須]': object.salary,
                '給与詳細': object.rawsalary,
                '勤務時間': object.timeshift,
                '最終学歴': object.education,
                '経験': object.experience,
                '待遇・福利厚生': object.benefits,
                '掲載期限': object.expirationdate,
                '最終掲載日': object.expdate,
                '追跡タグ': object.tracking_url,
                '画像URL': object.imageUrls,
                '採用予定人数': object.hires,
                'キーワード[カンマ区切り]': object.keywords,
                '作成日時[自動入力]': object.created_at,
            }
        )
    return response


class JobsImport(generic.FormView):
    template_name = 'jobs_import.html'
    success_url = reverse_lazy('list')
    form_class = CSVUploadForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_name'] = 'csvdownload'
        return ctx

    def form_valid(self, form):
        csvfile = io.TextIOWrapper(form.cleaned_data['file'])
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in reader:
            object, created = JobModel.objects.get_or_create(pk=row[0])
            object.title = row[1]
            object.date = row[2]
            object.company = row[3]
            object.country = row[4]
            object.postalcode = row[5]
            object.state = row[6]
            object.city = row[7]
            object.rawlocation = row[8]
            object.streetaddress = row[9]
            object.email = row[10]
            object.station = row[11]
            object.subwayaccess = row[12]
            object.category = row[13]
            object.jobtype = row[14]
            object.description = row[15]
            object.salary = row[16]
            object.rawsalary = row[17]
            object.timeshift = row[18]
            object.education = row[19]
            object.experience = row[20]
            object.benefits = row[21]
            object.expirationdate = row[22]
            object.expdate = row[23]
            object.tracking_url = row[24]
            object.imageUrls = row[25]
            object.hires = row[26]
            object.keywords = row[27]
            object.created_at = row[28]
            object.save()
        return super().form_valid(form)
