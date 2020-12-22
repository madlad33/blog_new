from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blogpost,Categories
from .forms import PostForm, EditForm,CategoryForm


# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
class Homeview(ListView):
    model = Blogpost
    template_name = 'home.html'
    ordering = ['-date_posted']

class BlogDetail(DetailView):
    model = Blogpost
    template_name = 'blog_detail.html'


class Addview(CreateView):
    model = Blogpost
    form_class = PostForm
    template_name = 'add_blog.html'
    # fields = ('title','author','body','title_tag')


class UpdateBlogView(UpdateView):
    model = Blogpost
    template_name = 'update_post.html'
    form_class = EditForm

    # fields = ['title','title_tag','body']
    def get_success_url(self):
        messages.success(self.request, 'Profile updated')
        return '/'


class DeleteBlogView(DeleteView):
    model = Blogpost
    template_name = 'delete_post.html'

    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class CreateCategoryView(CreateView):
    model = Categories
    template_name = 'add_category.html'
    form_class = CategoryForm