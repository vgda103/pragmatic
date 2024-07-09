from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accountapp.views import AccounrtDetailView, AccountUpdateView, AccountappDeleteView, hello_world, AccountCreateView

# 네임스페이스
app_name = 'accountapp'

urlpatterns = [
    # path( 주소명, views.py의 함수or클레스, 라우터에서 이름등록 )
    path( 'hello_world/', hello_world, name='hello_world' ),
    path( 'create/', AccountCreateView.as_view(), name='create' ),

    # 22강. 로그인/아웃 구현
    path( 'login/', 
        LoginView.as_view( template_name='accountapp/login.html' ), name='login' ),
    path( 'logout/', LogoutView.as_view(), name='logout' ),

    # 24강. DetailView
    # <int:pk> : / 뒤에 pk 이름의 int형 값을 받는다, 몇번 유저의정보
    path( 'detail/<int:pk>', AccounrtDetailView.as_view(), name='detail' ),      

    # 25강. UpdateView
    path( 'update/<int:pk>', AccountUpdateView.as_view(), name='update' ), 

    # 26강 DeleteView
    path( 'delete/<int:pk>', AccountappDeleteView.as_view(), name='delete' ),

]
