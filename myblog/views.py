from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Blogpost
from .forms import PostForm,EditForm

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
class Homeview(ListView):
    model=Blogpost
    template_name = 'home.html'

class BlogDetail(DetailView):
    model=Blogpost
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
        messages.success(self.request,'Profile updated')
        return '/'

