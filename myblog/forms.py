from django import forms
from .models import Blogpost

class PostForm(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields=('title','title_tag','author','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert title of the blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter the content you want to put up'}),



        }
class EditForm(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields=('title','title_tag','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert title of the blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter the content you want to put up'}),



        }