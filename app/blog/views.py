from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseServerError, HttpResponseNotFound
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.messages.views import SuccessMessageMixin


class WelcomeView(View):
    template_name = 'welcome.html'

    def get(self, request):
        return render(request, self.template_name)
        # 'welcome.html' 템플릿을 렌더링하여 HTTP 응답으로 반환합니다.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    # Post 모델의 모든 객체를 가져와서 'home.html' 템플릿에 넘겨주는 ListView입니다.


class BlogListView(ListView):
    model = Post
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    # Post 모델의 모든 객체를 가져와서 'blog_list.html' 템플릿에 넘겨주는 ListView입니다.


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'
    # Post 모델의 특정 객체를 가져와서 'blog_detail.html' 템플릿에 넘겨주는 DetailView입니다.

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except self.model.DoesNotExist:
            return HttpResponseNotFound("존재하지 않는 게시글입니다.")
            # 해당 게시글이 존재하지 않을 경우 "존재하지 않는 게시글입니다."라는 에러 메시지를 반환합니다.
        
        # 조회 수 증가
        self.object.view_count += 1
        self.object.save()
        # 게시글의 조회 수를 1 증가시키고 저장합니다.

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
        # 컨텍스트 데이터를 포함한 HTTP 응답을 반환합니다.


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_edit.html'
    # Post 모델의 특정 객체를 수정하기 위한 UpdateView입니다. 'post_edit.html' 템플릿을 사용합니다.

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # 폼이 유효한 경우 작성자를 현재 로그인한 사용자로 설정합니다.
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        # 현재 로그인한 사용자가 글의 작성자인지 확인하는 메서드입니다.


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog:home')
    # Post 모델의 특정 객체를 삭제하기 위한 DeleteView입니다. 'post_delete.html' 템플릿을 사용합니다. 삭제 후 'home' URL로 이동합니다.
    
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            error_message = '이런! 문제가 발생했습니다. 잠시 후 다시 시도 해 주세요. 지속될 경우 문의해주세요.'
            return HttpResponseServerError(error_message)
            # 예외가 발생할 경우 "이런! 문제가 발생했습니다..."라는 에러 메시지를 반환합니다.
        
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        # 현재 로그인한 사용자가 글의 작성자인지 확인하는 메서드입니다.


class PostSearchView(View):
    template_name = 'post_search.html'

    def get(self, request):
        query = request.GET.get('query', '')
        results = Post.objects.filter(title__icontains=query)
        context = {'query': query, 'results': results}
        return render(request, self.template_name, context)
        # 'query' 파라미터로 전달받은 검색어를 포함하는 게시글을 필터링하여 'post_search.html' 템플릿에 넘겨주는 HTTP 응답을 반환합니다.


class SignupView(View):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
        # 회원가입 폼을 사용하는 'signup.html' 템플릿을 렌더링하여 HTTP 응답으로 반환합니다.

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
        return render(request, self.template_name, {'form': form})
        # 폼이 유효한 경우 사용자를 생성하고 로그인한 후 'home' URL로 이동합니다.


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
        # 로그인 폼을 사용하는 'login.html' 템플릿을 렌더링하여 HTTP 응답으로 반환합니다.

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('blog:home')
        return render(request, self.template_name, {'form': form})
        # 폼이 유효한 경우 로그인한 후 'home' URL로 이동합니다.


class LogoutView(AuthLogoutView):
    next_page = 'blog:welcome'
    # 로그아웃한 후 'welcome' URL로 이동합니다.


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_write.html'
    success_url = '/blog/' 
    # Post 모델의 객체를 생성하기 위한 CreateView입니다. 'post_write.html' 템플릿을 사용합니다. 생성 후 'blog' URL로 이동합니다.

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # 폼이 유효한 경우 작성자를 현재 로그인한 사용자로 설정합니다.


class DeletedPostView(View):
    def get(self, request):
        return HttpResponseNotFound("존재하지 않는 게시글입니다.")
        # "존재하지 않는 게시글입니다."라는 에러 메시지를 반환합니다.


class ChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'change_password.html'
    form_class = PasswordChangeForm
    success_url = '/'
    success_message = "비밀번호 변경 성공!"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs
        # 폼 인스턴스를 생성할 때 추가 인수로 현재 로그인한 사용자를 전달합니다.

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return super().form_valid(form)
        # 폼이 유효한 경우 비밀번호를 변경하고 세션의 인증 해시를 업데이트합니다.
