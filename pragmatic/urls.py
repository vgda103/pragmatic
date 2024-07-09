"""
URL configuration for pragmatic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from articleapp.views import ArticleListView

urlpatterns = [

    # 45강 프로젝트 마무리 - 추가
    path( '', ArticleListView.as_view(), name='home' ),    
    # 'admin/' : URL에 대한 요청을 처리합니다.
    # admin.site.urls : 템플릿을 렌더링합니다.
    path('admin/', admin.site.urls),
    # include( 'accountapp.urls' ) : accountapp 내부에 있는 urls 에서 다시 분기한다
    path( 'accountapps/', include( 'accountapp.urls' ) ), 
    # 새로운 앱 profileapp의 주소 등록
    path( 'profiles/', include( 'profileapp.urls' ) ),
    # 새로운 앱 articleapp 주소 등록
    path( 'articles/', include( 'articleapp.urls' ) ),
    # 새로운 앱 commentapp 주소 등록
    path( 'commentapp/', include( 'commentapp.urls' ) ),
    # 새로운 앱 commentapp 주소 등록
    path( 'projectapp/', include( 'projectapp.urls' ) ), 
    # 새로운 앱 commentapp 주소 등록
    path( 'subscribeapp/', include( 'subscribeapp.urls' ) ), 

] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
# static: settings에서 정의한 MEDIA_URL과 MEDIA_ROOT 값을 사용해 정적 파일을 서빙한다
