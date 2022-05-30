from django.urls import path
from .views import login_func, logout_func, admin_navi_func, list_func, job_func, job_admin_func, JobDlete, JobUpdate, JobCreate, jobs_export, JobsImport, freewords, jobtype_list_func

urlpatterns = [
    path('login/', login_func, name='login'),
    path('logout/', logout_func, name='logout'),
    path('admin_navi/', admin_navi_func, name='admin_navi'),
    path('list/', list_func, name='list'),
    path('job/<uuid:pk>', job_func, name='job'),
    path('job_admin/<uuid:pk>', job_admin_func, name='job_admin'),
    path('delete/<uuid:pk>', JobDlete.as_view(), name='delete'),
    path('update/<uuid:pk>', JobUpdate.as_view(), name='update'),
    path('create/', JobCreate.as_view(), name='create'),
    path('jobs_export/', jobs_export, name='jobs_export'),
    path('jobs_import/', JobsImport.as_view(), name='jobs_import'),
    path('freewords/', freewords, name='freewords'),
    path('jobtype_list/', jobtype_list_func, name='jobtype_list'),
]
