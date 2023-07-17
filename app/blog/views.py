from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def home(request):
    # 페이지 제목과 블로그 입장하기 버튼을 렌더링
    return render(request, 'home.html')

def blog_list(request):
    blogs = Blog.objects.all()
    # 게시글 목록을 렌더링
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    # 게시글 상세 페이지를 렌더링
    return render(request, 'blog_detail.html', {'blog': blog})
