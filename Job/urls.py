# Created By Me

from django.urls import include , path
from . import views

app_name='Job'
urlpatterns = [
    path('',views.job_list , name = 'job_list'),
    path('add',views.add_job , name = 'add_job'),
    path('<str:slug>',views.job_detail , name = 'job_detail'),
    
]