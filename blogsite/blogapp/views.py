from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, BlogContent
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request,'index.html',{"name":"index"})

def contact(request):
    return render(request,'contact.html',{"name":"contact"})

class BlogpageView(ListView):
    model = BlogContent
    template_name = 'blogpage.html'

class BlogContentView(DetailView):
    model = BlogContent
    template_name = 'blogcontent.html'

class CreateBlogView(CreateView):
    model = BlogContent
    template_name = 'createblog.html'
    fields = '__all__'

class UpdateBlogView(UpdateView):
    model = BlogContent
    template_name = 'updateblog.html'
    fields = '__all__'

class DeleteBlogView(DeleteView):
    model = BlogContent
    template_name = 'deleteblog.html'
    success_url = reverse_lazy('blogpage')






