from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Insert your email'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insert your first name'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Insert your last name'}))


    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']


    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
       model=User
       fields=['username','email','first_name','last_name']

class EditUserPassword(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password' }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))

    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']