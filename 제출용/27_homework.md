# Django Form

###  학습해야 할 내용 

-  Django Class Based View

1.  Class Based View와 URL을 연결해 주기 위해서는 Function Based View와는 다르게, urls.py에서 views를
   import 하고 해당 모듈에 있는 View Class들을 path 함수로 넘겨주면서 특정 method를 호출하여 넘겨주
   어야 한다. 아래 예시의 (a)에 들어가야하는, 앞서 설명한 method를 작성하시오.

as_view()



1. Model과 연관된 Class Based View는 Django Framework에서 미리 만들어 놓은 Generic View Class들을
    import하고 이를 상속받아 작성한다. CRUD를 담당하는 대표적인 5가지 Generic View Class를 작성하고,
    각각의 역할을 간단하게 작성하시오.

ListView, CreateView, DetailView, UpdateView, DeleteView

