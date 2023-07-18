from django.urls import path
from . import views

app_name = "blog"

"""
/ 또는 /blog/ 로 접속했을 때, views.py 에서 home 함수를 실행하도록 설정

"""

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_page, name='blog_page'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]
