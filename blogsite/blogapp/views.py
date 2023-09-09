from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, BlogContent
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import decorators, mixins
from .forms import BlogContentForm

# Create your views here.

def index(request):
    return render(request,'index.html')

@decorators.login_required(login_url = '/auth/login')
def contact(request):
    return render(request,'contact.html',{"name":"contact"})

class BlogpageView(mixins.LoginRequiredMixin, ListView):
    login_url = '/auth/login'
    model = BlogContent
    template_name = 'blogpage.html'

class BlogContentView(mixins.LoginRequiredMixin, DetailView):
    login_url = '/auth/login'
    model = BlogContent
    template_name = 'blogcontent.html'

class CreateBlogView(mixins.LoginRequiredMixin, CreateView):
    login_url = '/auth/login'
    model = BlogContent
    template_name = 'createblog.html'
    form_class = BlogContentForm

class UpdateBlogView(mixins.LoginRequiredMixin, UpdateView):
    login_url = '/auth/login'
    model = BlogContent
    template_name = 'updateblog.html'
    form_class = BlogContentForm

class DeleteBlogView(mixins.LoginRequiredMixin, DeleteView):
    login_url = '/auth/login'
    model = BlogContent
    form_class = BlogContentForm
    template_name = 'deleteblog.html'
    success_url = reverse_lazy('blogpage')






