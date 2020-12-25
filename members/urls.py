from django.urls import path
from .views import UserRegisterView,UserEditView,ChangeUserPassword,password_success
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('editprofile/',UserEditView.as_view(),name='user_edit'),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),name='password_change')

    path('password/',ChangeUserPassword.as_view(),name='password_change'),
    path('password_success/',password_success,name='password_success'),
    ]