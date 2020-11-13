from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
# Create your views here.

class BlogListView(ListView):
    model=Post
    template_name='home.html'
class BlogDetailView(DetailView):
    model=Post
    template_name='detail.html'
class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']
class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
class BlogEditView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']
