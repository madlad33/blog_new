from django import forms
from .models import Blogpost,Categories

class PostForm(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields=('title','title_tag','author','categories','body')

        categories=Categories.objects.all().values_list('name','name')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert title of the blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'show',}),
            'categories':forms.Select(choices=categories,attrs={'class': 'form-control'}),
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

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields='__all__'
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert a valid category for the blog'}),

        }