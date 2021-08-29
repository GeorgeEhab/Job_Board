# Created By Me

from django.urls import include , path
from . import views
from . import api
app_name='Job'
urlpatterns = [
    path('',views.job_list , name = 'job_list'),
    path('add',views.add_job , name = 'add_job'),
    path('<str:slug>',views.job_detail , name = 'job_detail'),

    # api
    path('api/jobs', api.job_list_api , name = 'jobListAPI'),
    path('api/jobs/<int:id>', api.job_detail_api , name = 'jobDetailAPI'),
    
    # Class based view
    path('api/V2/jobs', api.JobList.as_view() , name = 'JobList'),
    path('api/V2/jobs/<int:id>', api.JobDetail.as_view() , name = 'JobDetail'),
    
]