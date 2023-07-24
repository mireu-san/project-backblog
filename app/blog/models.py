from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

"""
모델 (models.py):
- Post 모델에는 제목(title), 내용(content), 삭제 여부(is_deleted), 작성자(author), 작성 날짜(publication_date), 이미지(picture), 조회수(view_count) 필드가 있습니다.
"""

class Post(models.Model):
    title = models.CharField(max_length=255)  # 글의 제목을 저장하는 문자열 필드입니다.
    content = models.TextField(max_length=2000)  # 글의 내용을 저장하는 긴 문자열 필드입니다.
    is_deleted = models.BooleanField(default=False)  # 글이 삭제되었는지 여부를 저장하는 불리언 필드입니다. 기본값은 False로 설정되어 있습니다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글의 작성자를 나타내는 User 모델과의 외래 키 관계입니다. 작성자가 삭제되면 해당 글도 함께 삭제됩니다.
    publication_date = models.DateField(auto_now_add=True)  # 글이 작성된 날짜를 저장하는 날짜 필드입니다. auto_now_add=True로 설정되어 있어 글이 생성될 때 자동으로 현재 날짜가 저장됩니다.
    picture = models.ImageField(upload_to='post_pictures', blank=True, null=True)  # 글에 첨부되는 사진을 저장하는 이미지 필드입니다. 'post_pictures' 디렉토리에 업로드된 사진이 저장됩니다. 비어있거나 null일 수 있습니다.
    view_count = models.PositiveIntegerField(default=0)  # 글의 조회 수를 저장하는 양의 정수 필드입니다. 기본값은 0으로 설정되어 있습니다.
    
    def __str__(self):
        return self.title  # Post 모델의 인스턴스를 문자열로 표시할 때 사용되는 메서드입니다. 여기서는 글의 제목을 반환합니다.
    
    def get_absolute_url(self):
        """
        특정 포스트의 블로그 상세 페이지 URL을 반환하는 메서드입니다.
        
        Returns:
            str: 포스트의 블로그 상세 페이지 URL입니다.
        """
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})
        # reverse 함수는 뷰 이름과 인수를 기반으로 URL을 생성하는데 사용됩니다. 여기서는 'blog_detail' 뷰에 대한 URL을 생성하고, 포스트의 기본 키 (pk)를 인수로 전달합니다.


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)  # Renamed 'active' to 'is_approved'

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)