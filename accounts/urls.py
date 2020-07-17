from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='passwordReset'),
    path('register/', views.register, name='register'),
    # path('register', views.IndexView.as_view(), name='index'),
    # # ex: /polls/5/
    path('<int:pk>/', views.AccountDetail.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEdit.as_view(template_name='user/profile_edit.html'), name='profileEdit'),
    path('profile/create/', views.ProfileCreate.as_view(template_name='user/profile_create.html'),
         name='profileCreate'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='user/pass_change.html'),
         name='changePassword'),
    path('', views.AccountsList.as_view(), name='profilesList'),
    path('children/', views.ChildrenList.as_view(template_name='user/children.html'), name='children'),
    path('children/create/', views.ChildrenCreate.as_view(template_name='user/child_create.html'),
         name='childCreate'),
    path('children/<int:pk>/delete', views.ChildDelete.as_view(template_name='user/child_confirm_delete.html'),
         name='childDelete'),
    path('children/<int:pk>/edit', views.ChildEdit.as_view(template_name='user/child_edit.html'),
         name='childEdit'),
]
