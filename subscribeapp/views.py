from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import RedirectView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

# Create your views here.

# 웹 요청을 처리한다
@method_decorator( login_required, 'get' ) # 로그인 확인 처리
class SubscriptionView( RedirectView ):

    # 메소드 오버라이트
    # 완료된후 보내는 곳
    # self.request.GET에서 'project_pk' 값을 얻어서 해당 프로젝트의 상세 페이지로 되돌아감
    def get_redirect_url( self, *args, **kwargs ):
        return reverse( 'projectapp:detail', kwargs={ 
                        'pk' : self.request.GET.get( 'project_pk' ) } )
        pass # def get_redirect_url 끝

    # 메소드 오버라이트
    # get 요청을 처리한다
    def get( self, request, *args, **kwargs ):
        
        # project 값을 얻는다
        # get_object_or_404 : self.request.GET.get('project_pk') 값이 없으면 404패이지로 연결
        project = get_object_or_404( Project, pk=self.request.GET.get( 'project_pk' ) )
        # user 값을 얻는다
        user = self.request.user

        # 해당 user와 project 값을 갖고 있는 Subscription 객체를 찾는다
        subscription = Subscription.objects.filter( user=user, project=project )

        # subscription 값이 있으면
        if subscription.exists():
            # subscription 데이터를 삭제
            subscription.delete()
            pass # if subscription.exists 끝
        else:
            # subscription 값이 없으면 데이터를 저장
            Subscription( user=user, project=project ).save()
            pass # else 끝

        # 부모의 get을 실행후 리턴
        return super( SubscriptionView, self ).get( request, *args, **kwargs )
        pass # def get 끝

    pass # class SubscriptionVie 끝

# 웹 요청 처리
@method_decorator( login_required, 'get' ) # 로그인 확인
class SubscriptionListView( ListView ):

    # 참조할 모델 타입의 객체
    model = Article
    # 템플릿에서 클레스에 접근할 이름
    context_object_name = 'article_list'
    # 템플릿을 연결할 파일의 위치와 이름
    template_name = 'subscribeapp/list.html'
    # 한번에 보여줄 페이지 수
    paginate_by = 5

    # 특정 조건의 Article만 가져온다
    def get_queryset( self ):

        # user가 구독한 project를 가져온다
        # Subscription.objects 객체에서 user의 정보를 가져와 project의 값을 리스트로 만든다.
        projects = Subscription.objects.filter(
                     user=self.request.user ).values_list( 'project' )
        # 해당 프로젝트들에 속하는 Article 객체들을 가져온다
        article_list = Article.objects.filter( project__in=projects )
        return article_list

        pass # def get_queryset 끝

    pass # class SubscriptionListView 끝