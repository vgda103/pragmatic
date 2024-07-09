from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView

# 네임스페이스
app_name = 'articleapp'

# URL 패턴 목록을 등록합니다.
urlpatterns  = [
    
    # 기존
    # 'list/' URL에 대한 요청을 처리합니다.
    # TemplateView를 사용하여 'articleapp/list.html' 템플릿을 렌더링합니다.
    # 이 URL 패턴의 이름을 'list'로 지정합니다.
    # path( 'list/', TemplateView.as_view( 
    #     template_name='articleapp/list.html' ), name='list' ),
    # 36강 리스튜뷰 - 수정
    path( 'list/', ArticleListView.as_view(), name='list' ),

    # url 등록
    path( 'create/', ArticleCreateView.as_view(), name='create' ),
    # url 등록
    path( 'detail/<int:pk>', ArticleDetailView.as_view(), name='detail' ),
    # url 등록
    path( 'update/<int:pk>', ArticleUpdateView.as_view(), name='update' ),
    # url 등록
    path( 'delete/<int:pk>', ArticleDeleteView.as_view(), name='delete' ),
]