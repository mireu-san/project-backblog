from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

"""
1. 메인 페이지 구현
    - url : `/`
    - 페이지 제목과 블로그 입장하기 버튼이 있습니다.
2. Django admin을 이용하여 게시글 작성
    - 게시글은 제목, 내용으로 구성되어 있습니다.
    - `/admin` 을 이용하여 게시글을 작성해보세요.
3. 작성되어 있는 게시글 목록을 볼 수 있습니다.
    - url : `/blog`
    - 게시글들의 제목을 확인 할 수 있습니다.
4. 작성 되어있는 게시글 상세 페이지를 볼 수 있습니다.
    - url : `/blog/<int:id>` ex)`/blog/1, /blog/2,...`
    - 게시글의 제목/내용을 보는 기능입니다.
"""

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    # Save button to work
    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})
