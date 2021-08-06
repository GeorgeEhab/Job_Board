# Created By Me

from django.urls import include , path
from . import views

app_name='Job'
urlpatterns = [
    path('signup',views.signup , name = 'signup'),
    
]