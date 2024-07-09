from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

# 네임 스페이스
app_name = 'commentapp'

# url 패턴 목록을 등록
urlpatterns = [ 
    # create로 주소이름을 등록하고 view를 연결, 라우터 이름은 create 사용
    path( 'create/', CommentCreateView.as_view(), name='create' ),
    # delete 주소이름을 등록하고 view를 연결, 라우터 이름은 delete 사용
    path( 'delete/<int:pk>', CommentDeleteView.as_view(), name='delete' ),
]