# Created By Me

from django.urls import include , path
from . import views

app_name='Contact'
urlpatterns = [
    path('',views.send_message , name = 'contact'),
    
]