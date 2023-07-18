from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']  
    template_name = 'post_write.html'
    success_url = '/blog/' 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
