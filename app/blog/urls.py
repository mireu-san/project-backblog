from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]
