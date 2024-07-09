# 네임스페이스 용 변수
from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

# profileapp용 주소 등록
urlpatterns = [
    # create, 프로필 수정
    path( 'create/', ProfileCreateView.as_view(), name='create' ),
    # update, 주소에서 pk 라는 이름의 int형 값을 받는다
    path( 'update/<int:pk>', ProfileUpdateView.as_view(), name='update' ),

]