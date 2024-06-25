## Blog_Project_Page

---

### 프로젝트 개요

**블로그 프로젝트**는 사용자가 블로그 게시물을 생성, 수정, 조회, 삭제할 수 있는 종합적인 웹 애플리케이션입니다. 이 프로젝트는 Python과 Django를 사용하여 개발되었으며, API 엔드포인트를 위해 Django REST Framework(DRF)를 활용하였습니다. 사용자 인증, 프로필 관리, 댓글 기능, 좋아요 및 북마크 기능, 검색 및 필터링 기능을 포함하고 있습니다. 또한, Swagger UI를 통해 API 문서를 제공하여 개발자들이 API를 쉽게 이해하고 사용할 수 있도록 돕습니다.

### 프로젝트 리뷰

이 프로젝트를 통해 Django를 사용한 웹 개발에 대한 풍부한 경험을 쌓았습니다. 사용자 인증 구현, 사용자 프로필 관리, RESTful API 생성 방법을 학습하였습니다. 이 프로젝트는 백엔드 로직과 프론트엔드 템플릿의 통합, 사용자 상호작용 처리, PostgreSQL을 통한 데이터 지속성 보장 등을 포함합니다.

---

### 주요 기능

### 블로그 게시물 관리

- **생성, 조회, 수정, 삭제 (CRUD)** 기능 제공
- **댓글 시스템:** 사용자가 게시물에 댓글을 달 수 있음
- **좋아요 및 북마크:** 사용자가 게시물에 좋아요를 누르고 북마크할 수 있음
- **검색 기능:** 제목이나 내용으로 게시물 검색 가능

### 사용자 프로필

- **프로필 페이지:** 사용자의 게시물과 프로필 정보 표시
- **프로필 사진 업로드:** 사용자가 프로필 사진을 업로드 가능

### API 엔드포인트

- **RESTful API:** 게시물, 댓글, 프로필에 대한 전체 CRUD 작업을 API를 통해 제공
- **Swagger 문서화:** Swagger UI를 통한 상호작용 API 문서 제공

---

### 기술 스택

- **Python:** 백엔드 개발을 위한 주요 프로그래밍 언어
- **Django:** 애플리케이션 개발을 위한 웹 프레임워크
- **Django REST Framework (DRF):** API 엔드포인트 생성
- **PostgreSQL:** 사용자 및 게시물 데이터 저장을 위한 데이터베이스
- **Swagger:** API 문서화를 위한 도구

---

### 구현 과정

**1. 프로젝트 설정**

- Django 프로젝트 초기화 및 설정 구성
- 데이터 저장을 위한 PostgreSQL 설정

**2. 모델 개발**

- **Post 모델:** 블로그 게시물 (제목, 내용, 작성자, 타임스탬프 포함)
- **Comment 모델:** 게시물에 대한 댓글, Post 모델과 연동
- **Profile 모델:** 사용자 프로필 (소개글, 프로필 사진 포함)
- **Like 및 Bookmark 모델:** 사용자의 게시물 상호작용 추적

**3. 뷰 및 템플릿 생성**

- **게시물 뷰:** 게시물 목록, 상세, 생성, 수정, 삭제 뷰
- **프로필 뷰:** 사용자 프로필 상세 뷰
- **댓글 뷰:** 댓글 추가 및 목록 조회
- **상호작용 요소:** 좋아요 및 북마크 구현

**4. API 설정**

- 모델을 위한 시리얼라이저 생성
- CRUD 작업을 위한 API 뷰 개발
- Swagger를 통한 API 문서화 통합

**5. 사용자 경험 향상**

- 게시물 검색 기능 추가
- 프로필 사진 업로드 및 표시 기능 추가
- 댓글 및 좋아요 같은 액션에 대한 사용자 알림 구현

---

### 스크린샷

1. **메인 페이지**

![스크린샷 2024-06-20 오후 5.57.51.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f9f35de7-0091-4a79-819a-501ef9435828/029a14cf-f0cf-42a2-bf9f-bed842468600/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-20_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.57.51.png)

1. **게시물 상세 페이지**

![스크린샷 2024-06-20 오후 5.46.08.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f9f35de7-0091-4a79-819a-501ef9435828/007051b5-d8f6-4d9f-b50c-0451c47972e3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-20_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.46.08.png)

1. **게시물 작성 페이지**
    
    ![스크린샷 2024-06-20 오후 5.46.12.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f9f35de7-0091-4a79-819a-501ef9435828/c4c844f2-2ea2-44ed-9b6c-0af1bef039ff/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-20_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.46.12.png)
    

1. **관리자 페이지**
    
    ![스크린샷 2024-06-20 오후 5.46.22.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f9f35de7-0091-4a79-819a-501ef9435828/4af853ae-dde8-4af2-b24e-a0b433fc159c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-20_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.46.22.png)
    
2. **API 문서**
    
    ![스크린샷 2024-06-20 오후 5.46.51.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f9f35de7-0091-4a79-819a-501ef9435828/514af0ba-6faf-42d9-9de3-2b5eadda27ed/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-20_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.46.51.png)
    

![스크린샷 2024-06-20 오후 5.19.37.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f9f35de7-0091-4a79-819a-501ef9435828/f61dc337-242b-4a78-a0ba-3906681b6588/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-20_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.19.37.png)

---

### 주요 코드 스니펫 및 상세 설명

1. **게시물 저장**

```python
def save_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
```

**설명:**

- 요청 데이터를 기반으로 `PostForm`을 초기화합니다.
- 폼을 유효성 검사하고 게시물을 저장하며 현재 사용자와 연결합니다.
- 저장이 성공하면 게시물 상세 페이지로 리디렉션합니다.

1. **게시물에 댓글 달기**

```python
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})
```

**설명:**

- 기본 키를 통해 게시물 객체를 가져옵니다.
- 댓글 폼 제출을 처리하고 댓글을 게시물 및 사용자와 연결합니다.
- 댓글 저장 후 게시물 상세 페이지로 리디렉션합니다.

---

### 향후 개선 사항

- **답글 기능 추가:** 특정 댓글에 대한 답글 기능 구현
- **고급 검색 및 필터링:** 카테고리 및 태그를 기반으로 한 고급 검색 옵션 및 필터 추가
- **사용자 알림:** 댓글 및 좋아요 같은 사용자 액션에 대한 실시간 알림 통합

---

이 프로젝트는 Django를 사용하여 전체적인 웹 애플리케이션을 구축하는 능력을 보여줍니다. 모델 및 뷰 설정부터 RESTful API 생성, 상호작용 기능 구현까지 다양한 기능을 학습하고 적용할 수 있는 좋은 예시입니다.
