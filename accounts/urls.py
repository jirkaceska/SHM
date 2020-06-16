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
    path('', views.AccountsList.as_view(), name='profiles_list')
]
