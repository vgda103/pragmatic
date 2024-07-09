from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView


# 네임스페이스
app_name = 'projectapp'

urlpatterns = [
    # create로 주소이름을 등록하고 view를 연결, 라우터 이름은 create 사용
    path( 'create/', ProjectCreateView.as_view(), name='create' ),
    # list로 주소이름을 등록하고 view를 연결, 라우터 이름은 list 사용
    path( 'list/', ProjectListView.as_view(), name='list' ),
    # detail로 주소이름을 등록하고 view를 연결, 라우터 이름은 detail 사용
    path( 'detail/<int:pk>/', ProjectDetailView.as_view(), name='detail' ),
]