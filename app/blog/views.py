from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseServerError
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


class PostEditView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:home')

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            error_message = '이런! 문제가 발생했습니다. 잠시 후 다시 시도 해 주세요. 지속될 경우 문의해주세요.'
            return HttpResponseServerError(error_message)
        

class PostSearchView(View):
    template_name = 'post_search.html'

    def get(self, request):
        query = request.GET.get('query', '')
        results = Post.objects.filter(title__icontains=query)
        context = {'query': query, 'results': results}
        return render(request, self.template_name, context)  