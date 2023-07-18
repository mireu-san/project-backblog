from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    posts = Post.objects.all()
    # 페이지 제목과 블로그 입장하기 버튼을 렌더링
    return render(request, 'home.html', {'posts': posts})

# def blog_page(request):
#     posts = Post.objects.all()
#     return render(request, 'blog.html', {'posts': posts})

def blog_list(request):
    posts = Post.objects.all()
    # 게시글 목록을 렌더링
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # 게시글 상세 페이지를 렌더링
    return render(request, 'blog_detail.html', {'post': post})
