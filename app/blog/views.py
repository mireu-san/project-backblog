from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseServerError
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  
    template_name = 'post_write.html'
    success_url = '/blog/' 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # 현재 로그인한 유저가 작성자인지 확인
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:home')
    
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            error_message = '이런! 문제가 발생했습니다. 잠시 후 다시 시도 해 주세요. 지속될 경우 문의해주세요.'
            return HttpResponseServerError(error_message)
        
    # 현재 로그인한 유저가 작성자인지 확인
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    


class PostSearchView(View):
    template_name = 'post_search.html'

    def get(self, request):
        query = request.GET.get('query', '')
        results = Post.objects.filter(title__icontains=query)
        context = {'query': query, 'results': results}
        return render(request, self.template_name, context)


class SignupView(View):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
        return render(request, self.template_name, {'form': form})
    

class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('blog:home')
        return render(request, self.template_name, {'form': form})
    

class LogoutView(AuthLogoutView):
    next_page = 'blog:welcome'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_write.html'