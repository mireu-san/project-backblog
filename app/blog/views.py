from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Post


class WelcomeView(View):
    template_name = 'welcome.html'

    def get(self, request):
        return render(request, self.template_name)


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class BlogListView(ListView):
    model = Post
    template_name = 'blog_list.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'