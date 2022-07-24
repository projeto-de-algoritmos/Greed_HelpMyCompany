from django.urls import path
from . import views

from django.conf import settings


urlpatterns = [
    path('',views.home, name='home'),
    path('getTime_table', views.getTime_table, name='getTime_table'),
    path('getFile', views.getFile, name='getFile')
    
]