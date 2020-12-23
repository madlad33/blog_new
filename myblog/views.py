from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blogpost, Categories
from .forms import PostForm, EditForm, CategoryForm


# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
class Homeview(ListView):
    model = Blogpost
    template_name = 'home.html'
    ordering = ['-date_posted']

    def get_context_data(self, *args,**kwargs):
        cat_menu = Categories.objects.all()
        context = super(Homeview, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class BlogDetail(DetailView):
    model = Blogpost
    template_name = 'blog_detail.html'



class Addview(CreateView):
    model = Blogpost
    form_class = PostForm
    template_name = 'add_blog.html'
    # fields = ('title','author','body','title_tag')
    def get_success_url(self):
        return reverse_lazy('home')


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


def CategoryUrlView(request, category):
    post_by_category = Blogpost.objects.filter(categories__iexact=category.replace('-',' '))

    return render(request, 'view_by_category.html', {'category':category.replace('-',' '), 'post_by_category': post_by_category})
