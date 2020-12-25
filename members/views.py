from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy, reverse
# Create your views here.
from .forms import SignUpForm,EditProfileForm,EditUserPassword
from django.contrib.auth.views import PasswordChangeView
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    def get_success_url(self):
        return reverse('home')
    def get_object(self, queryset=None):
        return self.request.user


class ChangeUserPassword(PasswordChangeView):
    form_class = EditUserPassword
    def get_success_url(self):
        return reverse_lazy('home')
    template_name = 'registration/change_password.html'

def password_success(request,render):
    render(request,'password_success.html',{})