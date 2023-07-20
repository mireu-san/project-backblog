# 환영합니다!

# 1. 프로젝트 제목
'소설 리뷰 블로그'가 본 프로젝트의 주제 입니다.

# 2. 프로젝트 설명.
블로그 기능을 제공하는 웹 애플리케이션입니다.

## 2.1 주요 기능

- CRUD 기능: 블로그 게시물의 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 기능을 제공합니다.
- 회원가입 기능: 사용자는 회원으로 가입하여 블로그를 이용할 수 있습니다.
- 비밀번호 변경 기능: 회원은 자신의 비밀번호를 변경할 수 있습니다.
- 추가 예정 기능: 근시일에 방명록, 대댓글 기능 등이 추가될 예정입니다.

## 2.2 기술 스택

프로젝트는 다음과 같은 기술을 사용하여 개발되었습니다:

- 프레임워크: Django (4.2.3)
- 데이터베이스: SQLite3
- 언어: Python, HTML/CSS
- 기타 라이브러리: [black formatter, graphviz, Pillow, django-extensions]
- [자세한 것은 requirements.txt 를 참고해주세요.]
## 설치 및 실행

아래의 명령어를 사용하여 프로젝트를 설치하고 실행할 수 있습니다:

```windows powershell 기준
# 가상환경 설정 및 활성화
python -m venv backblog
source backblog/bin/activate

# 의존성 설치
pip install -r requirements.txt

# 데이터베이스 마이그레이션
python manage.py migrate

# 개발 서버 실행
project-backblog\app\python manage.py runserver

# 실행 주소
http://127.0.0.1:8000/
```
# 구동 예시
## 1. 최초의 화면
![welcome page](app/a.png)

## 2. 블로그 진입 시 화면.
home.html 의 template file 을 렌더링 한 후, blog_list.html 쪽에서 등록된 post 목록을 이곳에 표시합니다.
![blog home.html](app/b.png)

## 3. 비 로그인 상태
![비 로그인 상태](app/d.png)

## 4. 회원가입
![회원가입](app/e.png)

## 5. 사진 미디어, 그리고 로그인 작성자 일치 시 수정/삭제 권한.
![몰루 사진](app/c.png)

## 6. 비 로그인 및 유저 인증이 일치하지 않는 경우, 수정 삭제 숨김.
![비 로그인 시 수정 삭제 숨김](app/f.png)

ERDs
![erd database diagram](app/erd_graphviz.png)