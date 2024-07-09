# from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView
# from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

# Create your views here.

# 웹 요청을 처리할 클레스
class CommentCreateView( CreateView ):
        
    # 참조 할 Model 타입 클래스
    model = Comment
    # 만들 폼을 참조 할 객체
    form_class = CommentCreationForm
    # 렌더링할 템플릿을 적용시킬 html 파일 경로
    template_name = 'commentapp/create.html'

    # 유효성 검사를 통과한 경우 실행되는 메서드 오버라이드, 
    # 데이터베이스에 게시물 작성자를 현재 사용자로 설정하고 저장합니다.
    def form_valid(self, form) -> HttpResponse:

        # 임시저장
        temp_comment = form.save( commit=False )
        # 코맨트의 내용을 가져온다
        # article_pk = commentapp/templates/commentapp/create.htm 에서
        # <input type="hidden" name="article.pk" value="{{ article.pk }}" >의 article.pk 값
        temp_comment.article = Article.objects.get( pk=self.request.POST[ 'article_pk' ] )
        # temp_comment.article = get_object_or_404( Article, 
        #                                          pk=self.request.POST.get('article_pk') )
        # 코맨트 작성자를 받아온다
        temp_comment.writer = self.request.user
        # 내용을 DB에 저장
        temp_comment.save()

        # 부모 클래스의 form_valid 메소드를 호출하고 그 결과를 반환
        return super().form_valid(form)
        pass # def form_valid 끝

    # 요청이 성공적으로 완료된 후 리디렉션할 URL 반환
    def get_success_url( self ):
        # 첫번째인자값 주소로 재접속, kwargs : pk 값을 URL 인자로 포함
        return reverse( 'articleapp:detail', kwargs={ 'pk' : self.object.article.pk } )
        pass # def get_success_url 끝

    pass # class CommentCreateView 끝

# 웹 요청을 처리할 클레스
@method_decorator( comment_ownership_required, 'get' )
@method_decorator( comment_ownership_required, 'post' )
class CommentDeleteView( DeleteView ):

    # 참조 할 Model 타입 클래스
    model = Comment
    # 템플릿에(html파일) 전달될 컨텍스트의 변수명을 설정
    context_object_name = 'target_comment'
    # 렌더링할 템플릿을 적용시킬 html 파일 경로
    template_name = 'commentapp/delete.html'

    # 동작 완료시 이동할 주소 설정
    def get_success_url( self ):
        return reverse( 'articleapp:detail', kwargs={ 'pk' : self.object.article.pk } )
        pass # def get_success_url 끝

    pass # class CommentDeleteView 끝