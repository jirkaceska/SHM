from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http.response import HttpResponse

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.camps_list, name='index'),
    path('camps/', views.camps_list, name='index_long'),
    path('camps/<int:pk>', views.TaskDetail.as_view(), name='detail'),
]
