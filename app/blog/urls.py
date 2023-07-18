from django.urls import path
from . import views

app_name = "blog"

"""
/ 또는 /blog/ 로 접속했을 때, views.py 에서 home 함수를 실행하도록 설정

"""

urlpatterns = [
    # 최초의 화면을 welcome.html 로 설정
    path('welcome/', views.welcome, name='welcome'),
    
    # blog 화면에 진입 시 모습. home.html 을 렌더링
    path('', views.home, name='home'),
    
    # blog 의 각 post 별, 고유 id 값을 가지고 있는 url 을 생성
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]

    # path('list/', views.blog_list, name='blog_list'),
    # path('blog/', views.blog_page, name='blog_page'),