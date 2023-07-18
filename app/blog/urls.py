from django.urls import path
from . import views

app_name = "blog"

"""
/ 또는 /blog/ 로 접속했을 때, views.py 에서 home 함수를 실행하도록 설정

"""

urlpatterns = [
    # 최초의 화면을 welcome.html 로 설정
    path('', views.welcome, name='welcome'),
    
    # blog 화면에 진입 시 모습. home.html 을 렌더링
    path('blog/', views.home, name='home'),

    # welcome.html 에 위치한 블로그 입장하기 버튼을 눌렀을 때, home.html에 표시 될 blog_list.html 을 렌더링
    path('list/', views.blog_list, name='blog_list'),

    # blog 의 각 post 별, 고유 id 값을 가지고 있는 url 을 생성
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]

    
    # path('blog/', views.blog_page, name='blog_page'),