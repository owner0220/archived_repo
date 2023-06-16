# 사용자인증/사용자권한관리

### 학습해야 할 내용

- Django auth

1. 로그인을 한 사용자만 게시물을 작성할 수 있도록 코드를 작성하려고 한다. 빨간 박스에 들어갈 코드를 작성하세요.

**정답 :**

**`from django.views.decorators.http import require_GET`**

**`@require_GET()` ** 





2. Board 모델에 게시물을 작성한 사람을 저장할 칼럼을 추가하려고 한다. 이를 위해 필요한 모듈과 ForeignKey() 에 넣어야 할 인자를 작성하세요.

**정답 :**

**settings**

**settings.AUTH_USER_MODEL**

