# 환영합니다!
- 현재 작업중입니다.

# 요약.
- 0단계: Django Admin을 이용한 게시글 읽기 및 메인페이지 구현.
- 1단계: 블로그 CRUD 기능 구현.
- 2단계: 로그인/회원가입 기능을 이용하여 블로그 구현.
- 3단계: 블로그 기능 외 추가 기능 작성 및 배포.

# 주제.
건전하고 가볍게 읽을 수 있는 소설 리뷰 블로그.


README.md
================

이것은 Django 프레임워크를 사용하여 블로그 기능을 구현한 프로젝트에 대한 README 파일입니다. 이 프로젝트는 블로그 관련 다양한 Django 기능의 흐름과 기능을 보여줍니다.

폴더 구조
----------------

프로젝트의 폴더 구조는 다음과 같습니다:

```
├─ .gitignore
├─ .vscode
│  └─ settings.json
├─ app
│  ├─ app
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  └─ __init__.py
│  ├─ blog
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_post_is_deleted.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  ├─ blog
│  │  │  ├─ blog_detail.html
│  │  │  ├─ blog_list.html
│  │  │  ├─ change_password.html
│  │  │  ├─ home.html
│  │  │  ├─ login.html
│  │  │  ├─ post_404.html
│  │  │  ├─ post_delete.html
│  │  │  ├─ post_edit.html
│  │  │  ├─ post_form.html
│  │  │  ├─ post_search.html
│  │  │  ├─ post_write.html
│  │  │  ├─ signup.html
│  │  │  └─ welcome.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  └─ manage.py
├─ backblog
│  ├─ Include
│  ├─ Lib
│  ├─ pyvenv.cfg
│  └─ Scripts
│     ├─ activate
│     ├─ activate.bat
│     ├─ Activate.ps1
│     ├─ black.exe
│     ├─ blackd.exe
│     ├─ deactivate.bat
│     ├─ django-admin.exe
│     ├─ pip.exe
│     ├─ pip3.10.exe
│     ├─ pip3.11.exe
│     ├─ pip3.exe
│     ├─ python.exe
│     ├─ pythonw.exe
│     └─ sqlformat.exe
├─ projectblog
│  ├─ app
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  └─ __init__.py
│  ├─ blog
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  └─ manage.py
└─ README.md
```

URL 구성 (urls.py)
---------------------------

블로그 앱의 URL 구성은 `urls.py` 파일에 정의되어 있습니다. URL 및 해당하는 뷰는 다음과 같습니다:

- 루트 URL `/` 및 `/blog/`은 각각 `HomeView` 및 `WelcomeView`에 매핑됩니다.
- `/list/` URL은 `BlogListView`를 통해 `blog_list.html` 템플릿을 렌더링합니다.
- `/blog/<int:pk>/` URL은 `BlogDetailView`를 사용하여 블로그 게시물의 상세 보기를 표시합니다.
- `/blog/write/` URL은 `PostCreateView`를 사용하여 새로운 블로그 게시물을 생성합니다.
- `/blog/edit/<int:pk>/` URL은 `PostEditView`를 사용하여 기존의 블로그 게시물을 수정합니다.
- `/blog/delete/<int:pk>/` URL은 `PostDeleteView`를 사용하여 블로그 게시물을 삭제합니다.
- `/blog/search/` URL은 `PostSearchView`를 사용하여 블로그 게시물을 검색합니다.
- `/login/` URL은 `LoginView`를 사용하여 사용자 로그인을 처리합니다.
- `/logout/` URL은 사용자 로그아웃을 처리합니다.
- `/signup/` URL은 `SignupView`를 사용하여 사용자 회원가입을 처리합니다.
- `/blog/deleted/` URL은 삭제된 게시물에 대한 사용자 지정 메시지를 표시합니다.
- `/change_password/` URL은 `ChangePasswordView`를 사용하여 사용자의 비밀번호를 변경합니다.

모델

 (models.py)
--------------------

`Post` 모델은 블로그 게시물을 나타내며 다음과 같은 필드를 포함합니다:

- `title`: 게시물 제목
- `content`: 게시물 내용
- `is_deleted`: 게시물 삭제 여부
- `author`: 게시물 작성자(User 모델과의 외래 키 관계)
- `publication_date`: 게시물 작성 날짜
- `picture`: 게시물 이미지
- `view_count`: 게시물 조회수

뷰 (views.py)
----------------

- `WelcomeView`: `welcome.html` 템플릿을 렌더링하여 사용자에게 초기 화면을 보여줍니다.
- `HomeView`: `home.html` 템플릿을 렌더링하여 최신 블로그 게시물을 보여줍니다.
- `BlogListView`: `blog_list.html` 템플릿을 렌더링하여 모든 블로그 게시물을 보여줍니다.
- `BlogDetailView`: `blog_detail.html` 템플릿을 렌더링하여 특정 블로그 게시물의 세부 정보를 보여줍니다.
- `PostEditView`: `post_edit.html` 템플릿을 렌더링하여 블로그 게시물을 수정합니다.
- `PostDeleteView`: `post_delete.html` 템플릿을 렌더링하여 블로그 게시물을 삭제합니다.
- `PostSearchView`: `post_search.html` 템플릿을 렌더링하여 블로그 게시물을 검색합니다.
- `SignupView`: `signup.html` 템플릿을 렌더링하여 사용자 회원가입을 처리합니다.
- `LoginView`: `login.html` 템플릿을 렌더링하여 사용자 로그인을 처리합니다.
- `LogoutView`: 사용자 로그아웃을 처리합니다.
- `PostCreateView`: `post_write.html` 템플릿을 렌더링하여 새로운 블로그 게시물을 생성합니다.
- `DeletedPostView`: 삭제된 게시물에 대한 사용자 정의 메시지를 표시합니다.
- `ChangePasswordView`: `change_password.html` 템플릿을 렌더링하여 사용자의 비밀번호를 변경합니다.

폼 (forms.py)
-----------------

`PostForm` 폼 클래스는 `forms.py` 파일에 정의되어 있습니다. 이 폼은 `PostCreateView`와 `PostEditView`에서 블로그 게시물의 생성 및 수정에 사용됩니다.

설정 (settings.py)
------------------------

`settings.py` 파일에는 블로그 프로젝트의 Django 설정이 포함되어 있습니다. 데이터베이스, 정적 파일, 미디어 파일, 설치된 앱, 미들웨어, 템플릿, 인증 등의 설정이 포함되어 있습니다.

