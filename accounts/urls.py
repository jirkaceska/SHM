from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('register/', views.register, name='register'),
    # path('register', views.IndexView.as_view(), name='index'),
    # # ex: /polls/5/
    path('<int:pk>/', views.AccountDetail.as_view(), name='profile'),
    path('profile/edit', views.ProfileEdit.as_view(template_name='user/profile_edit.html'), name='profile_edit'),
    path('profile/create', views.ProfileCreate.as_view(template_name='user/profile_create.html'), name='profile_create'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='user/pass_change.html'),
         name='change_password'),
    path('', views.AccountsList.as_view(), name='profiles_list'),
    path('children', views.ChildrenCreate.as_view(template_name='user/children.html'), name='children'),
]
