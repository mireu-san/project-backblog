from django.urls import path
from .views import (
    HomeView, 
    BlogListView,
    BlogDetailView, 
    WelcomeView, 
    PostCreateView,
    PostEditView,
    PostDeleteView,
    PostSearchView,
    LoginView,
    LogoutView,
    SignupView,
    DeletedPostView,
    ChangePasswordView,

    PostListView, 
    PostDetailView,
)

app_name = "blog"

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    # 최초의 화면을 'welcome.html'로 설정하는 URL 패턴입니다.

    path('blog/', HomeView.as_view(), name='home'),
    # '/blog/' URL에 대해 'HomeView'를 사용하여 'home.html'을 렌더링하는 URL 패턴입니다.

    path('list/', BlogListView.as_view(), name='blog_list'),
    # '/list/' URL에 대해 'BlogListView'를 사용하여 'blog_list.html'을 렌더링하는 URL 패턴입니다.

    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    # '/blog/<int:pk>/' URL에 대해 'BlogDetailView'를 사용하여 'blog_detail.html'을 렌더링하는 URL 패턴입니다.
    # <int:pk>는 글의 고유 id 값을 나타냅니다. 조회수 기능이 구현되어 있습니다.

    path('blog/create/', PostCreateView.as_view(), name='post_create'),
    # '/blog/create/' URL에 대해 'PostCreateView'를 사용하여 'post_create.html'을 렌더링하는 URL 패턴입니다.
    # 새로운 글을 작성하는 기능입니다.

    path('blog/edit/<int:pk>/', PostEditView.as_view(), name='post_edit'),
    # '/blog/edit/<int:pk>/' URL에 대해 'PostEditView'를 사용하여 'post_edit.html'을 렌더링하는 URL 패턴입니다.
    # 글을 수정하는 기능입니다. <int:pk>는 수정할 글의 고유 id 값을 나타냅니다.

    path('blog/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    # '/blog/delete/<int:pk>/' URL에 대해 'PostDeleteView'를 사용하여 'post_delete.html'을 렌더링하는 URL 패턴입니다.
    # 글을 삭제하는 기능입니다. <int:pk>는 삭제할 글의 고유 id 값을 나타냅니다.

    path('blog/search/', PostSearchView.as_view(), name='post_search'),
    # '/blog/search/' URL에 대해 'PostSearchView'를 사용하여 'post_search.html'을 렌더링하는 URL 패턴입니다.
    # 글을 검색하는 기능입니다.

    path('login/', LoginView.as_view(), name='login'),
    # '/login/' URL에 대해 'LoginView'를 사용하여 'login.html'을 렌더링하는 URL 패턴입니다.
    # 로그인 기능입니다.

    path('logout/', LogoutView.as_view(), name='logout'),
    # '/logout/' URL에 대해 'LogoutView'를 사용하여 로그아웃 기능을 수행하는 URL 패턴입니다.

    path('signup/', SignupView.as_view(), name='signup'),
    # '/signup/' URL에 대해 'SignupView'를 사용하여 'signup.html'을 렌더링하는 URL 패턴입니다.
    # 회원가입 기능입니다.

    path('blog/deleted/', DeletedPostView.as_view(), name='deleted_post'),
    # '/blog/deleted/' URL에 대해 'DeletedPostView'를 사용하여 삭제된 게시글에 대한 경고문을 렌더링하는 URL 패턴입니다.

    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    # '/change_password/' URL에 대해 'ChangePasswordView'를 사용하여 'change_password.html'을 렌더링하는 URL 패턴입니다.
    # 비밀번호 변경 기능입니다.

    # 댓글 기능


]
