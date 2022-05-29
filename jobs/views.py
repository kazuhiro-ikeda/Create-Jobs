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
from .models import Jobs
from .forms import JobsForm, JobsImportForm
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


def logout_func(request):
    logout(request)
    return redirect('login')


@login_required()
def admin_navi_func(request):
    template_name = 'admin_navi.html'
    return render(request, 'admin_navi.html')


def list_func(request):
    object_list = Jobs.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def job_func(request, pk):
    object = get_object_or_404(Jobs, pk=pk)
    return render(request, 'job.html', {'object': object})


def job_admin_func(request, pk):
    object = get_object_or_404(Jobs, pk=pk)
    return render(request, 'job_admin.html', {'object': object})


class JobDlete(DeleteView):
    template_name = 'delete.html'
    model = Jobs
    success_url = reverse_lazy('list')


class JobUpdate(UpdateView):
    template_name = 'update.html'
    model = Jobs
    form_class = JobsForm

    def get_success_url(self):
        return reverse('job', kwargs={"pk": self.object.pk})


class JobCreate(CreateView):
    template_name = 'create.html'
    model = Jobs
    form_class = JobsForm

    def get_success_url(self):
        return reverse('job', kwargs={"pk": self.object.pk})


def jobs_export(request):
    response = HttpResponse(content_type='text/csv;')
    filename = urllib.parse.quote((u'jobs.csv'))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    fieldnames = [
        'ID[編集不可]',
        'タイトル[必須]',
        '会社名[必須]',
    ]
    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()
    for object in Jobs.objects.all():
        writer.writerow(
            {
                'ID[編集不可]': object.id,
                'タイトル[必須]': object.title,
                '会社名[必須]': object.company
            }
        )
    return response


class JobsImport(generic.FormView):
    template_name = 'jobs_import.html'
    success_url = reverse_lazy('list')
    form_class = JobsImportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'csvdownload'
        return context

    def form_valid(self, form):
        csvfile = io.TextIOWrapper(form.cleaned_data['file'])
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in reader:
            """
            このコードも動作
            key = row[0] if row[0] else None
            object, created = Jobs.objects.get_or_create(id=key)
            """

            if row[0]:
                object = Jobs.objects.get(id=row[0])
            else:
                object = Jobs.objects.create()

            object.title = row[1]
            object.company = row[2]
            object.save()
        return super().form_valid(form)