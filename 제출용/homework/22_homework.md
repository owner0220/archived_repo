# Media & Static Files

### 학습해야 할 내용

- 미디어 파일과 정적 파일



1. attachment column에 파일을 저장하려고 한다. 아래의 (a)에 정의 해야 하는 field는?



**정답 : TextField()**





2. 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 내부의 '/uploaded_files'로 지정하고자
   한다. 이 때, settings.py에 작성해야 할 설정 2가지와 이것이 의미하는 바를 간략하게 작성하시오.



**정답 :**

- MEDIA_URL = "/uploaded_files/"                                 **URL에서 요청할 주소**
- MEDIA_ROOT = os.path.join(BASE_DIR,"media")      **파일이 저장될 위치**





3. 개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더 내부의 '/assets'에 있
   다. '이 폴더 안에 정적 파일이 있다.'라고 Django 프로젝트에게 알려주기 위해서 settings.py에 작성해야
   하는 설정을 작성하시오.



**정답 :**

STATICFILES_DIRS  = os.path.join(BASE_DIR,"assets")   **파일 위치를 등록해줘야 한다.**