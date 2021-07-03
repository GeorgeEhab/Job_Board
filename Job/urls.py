# Created By Me

from django.urls import include , path
from . import views

app_name='Job'
urlpatterns = [
    path('',views.job_list),
    path('<str:slug>',views.job_detail , name='job_detail')
]