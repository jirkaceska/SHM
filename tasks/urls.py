from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http.response import HttpResponse

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.camps_list, name='index'),
    path('camps/', views.camps_list, name='indexLong'),
    path('camps/<int:pk>/', views.task_info, name='taskInfo'),
    path('camps/<int:pk>/applications/', views.TaskApplicationsList.as_view(
        template_name='tasks/signable_task_applications.html'), name='taskApplications'),
    path('camps/<int:pk>/tasks/', views.TaskApplicationTasks.as_view(
        template_name='tasks/signable_task_tasks.html'), name='taskTasks'),
    path('applications/<int:pk>/team/', views.task_team, name='taskTeam'),
    path('applications/<int:task_id>/team/<int:user_id>/delete/', views.task_team_delete, name='taskTeamDelete'),
    path('applications/', views.ApplicationsList.as_view(template_name='applications/application_list.html'),
         name='applications'),
    path('applications/<int:pk>/delete/', views.ApplicationSuspend.as_view(
        template_name='applications/application_delete_confirm.html'), name='applicationDelete'),
    path('applications/<int:pk>/edit/', views.ApplicationEdit.as_view(
        template_name='applications/application_edit.html'), name='applicationEdit'),
    path('tasks/<int:pk>/edit/', views.TaskEdit.as_view(
        template_name='tasks/task_edit.html'), name='taskEdit'),
    path('tasks/<int:pk>/create/', views.TaskCreate.as_view(
        template_name='tasks/task_create.html'), name='taskCreate'),
]
