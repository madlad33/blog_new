from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Blogpost
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
class Homeview(ListView):
    model=Blogpost
    template_name = 'home.html'

class BlogDetail(DetailView):
    model=Blogpost
    template_name = 'blog_detail.html'
