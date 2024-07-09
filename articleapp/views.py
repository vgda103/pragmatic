from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm

# 웹 요청을 처리하는 클레스들
# TemplateView: 단순한 템플릿 렌더링.
# ListView: 모델 객체의 목록을 보여줌.
# DetailView: 모델 객체의 세부 정보를 보여줌.
# CreateView: 모델 객체를 생성하는 폼을 제공하고 처리.
# UpdateView: 모델 객체를 업데이트하는 폼을 제공하고 처리.
# DeleteView: 모델 객체를 삭제하는 기능을 제공

# Create your views here.

# 웹 요청을 처리할 클레스
@method_decorator( login_required, 'get' )  # GET 요청에 대해 로그인 인증 확인
@method_decorator( login_required, 'post' ) # POST 요청에 대해 로그인 인증 확인
class ArticleCreateView( CreateView ):

    # 참조 할 Model 타입 클래스
    model = Article
    # 만들 폼을 참조 할 객체
    form_class = ArticleCreationForm
    # 렌더링할 템플릿을 적용시킬 html 파일 경로
    template_name = 'articleapp/create.html'    

    # 유효한 경우 실행되는 메소드 오버라이드, db의 작성자를 현재 사용자로 설정하고 데이터를 저장
    def form_valid( self, form ):
        
        # 폼 데이터를 임시 저장하고 객체를 반환
        temp_article = form.save( commit=False )
        # 임시 객체의 writer 필드를 현재 사용자로 설정
        # 게시물의 내용을 가져온다
        temp_article.writer = self.request.user
        # db 에 데이터 저장
        temp_article.save()
        
        # 부모 클래스의 form_valid 메소드를 호출하고 그 결과를 반환
        return super().form_valid( form )
        pass # def form_valid 끝

     # 요청이 성공적으로 완료된 후 리디렉션할 URL 반환
    def get_success_url( self ):
        # articleapp:detail 주소로 재접속, kwargs : pk 값을 URL 인자로 포함
        return reverse( 'articleapp:detail', kwargs={ 'pk':self.object.pk } )

    pass # class ArticleCreationView 끝

# 37강. Mixin 에서 FormMixin 상속 추가
# 새로만든 Commentapp을 delete.html에 추가하는대,
# ArticleDetailView에는 form이 없어서 FormMixin을 상속 받아서 form 사용
# 웹 요청을 처리할 클레스
class ArticleDetailView( DetailView, FormMixin ):

    # 참조 할 Model 타입 클래스
    model = Article
    # 만들 폼을 참조 할 객체
    form_class = CommentCreationForm # 37강. Mixin 에서 추가
    # 템플릿에 전달될 컨텍스트의 변수명을 설정
    context_object_name = 'target_article'
    # 렌더링할 템플릿을 적용시킬 html 파일 경로
    template_name = 'articleapp/detail.html'

    pass # class ArticleDetailView 끝

# 웹 요청을 처리할 클레스
@method_decorator( article_ownership_required, 'get' )  # GET 요청에 대해 로그인 인증 확인
@method_decorator( article_ownership_required, 'post' ) # POST 요청에 대해 로그인 인증 확인
class ArticleUpdateView( UpdateView ):

    # 참조 할 Model 타입 클래스
    model = Article
    # 템플릿에 전달될 컨텍스트의 변수명을 설정
    context_object_name = 'target_article'
    # 만들 폼을 참조 할 객체
    form_class = ArticleCreationForm
    # 렌더링할 템플릿을 적용시킬 html 파일 경로
    template_name = 'articleapp/update.html'    

    # 요청이 성공적으로 완료된 후 리디렉션할 URL 반환
    def get_success_url( self ):
        # articleapp:detail 주소로 재접속, kwargs : pk 값을 URL 인자로 포함
        return reverse( 'articleapp:detail', kwargs={ 'pk':self.object.pk } )

    pass # class ArticleCreationView 끝

# 웹 요청 처리 클레스
class ArticleDeleteView( DeleteView ):

    # 참조 할 Model 타입 클래스
    model = Article
    # 템플릿에 전달될 컨텍스트의 변수명을 설정
    context_object_name = 'target_article'
    # 완료한후 이동할 url
    success_url = reverse_lazy( 'articleapp:list' )
    # 렌더링할 템플릿을 적용시킬 html 파일 경로
    template_name = 'articleapp/delete.html'
    
    pass # class ArticleDeleteView 끝

# 36강 리스트뷰
# 웹 요청 처리 클래스
class ArticleListView( ListView ):

    # 참조 할 Model 타입 클래스
    model = Article
    # 템플릿에 전달될 컨텍스트의 변수명을 설정
    context_object_name = 'article_list'
    # 랜더링할 템플릿을 적용시킬 html 파일경로
    template_name = 'articleapp/list.html'
    # 한 페이지당 보여질 항목의 수
    paginate_by = 5

    pass # class ArticleListView 끝