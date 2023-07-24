from django import forms
from .models import Post, Comment

"""
폼 (forms.py):
- PostForm 폼 클래스가 존재합니다.
"""

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'picture']

        # 'Post' 모델을 기반으로 폼을 생성하는 'PostForm'입니다.

        # 'Meta' 클래스를 사용하여 모델과 폼의 메타데이터를 정의합니다.
        # 'model' 속성에는 폼이 생성될 모델인 'Post'를 지정합니다.

        # 'fields' 속성은 폼에서 사용될 필드들을 지정합니다.
        # 'title', 'content', 'picture' 필드가 폼에 표시됩니다.


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Comment 모델의 필드를 기반으로 합니다.