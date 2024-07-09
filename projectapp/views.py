from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreainoneForm
from projectapp.models import Project
from subscribeapp.models import Subscription

# Create your views here.

# 웹에서 요청을 처리 클레스
# 게시물을 만드는 클레스
@method_decorator( login_required, 'get' )
@method_decorator( login_required, 'post' )
class ProjectCreateView( CreateView ):

    # 참조할 모델 클레스
    model = Project
    # 참조할 폼클레스
    form_class = ProjectCreainoneForm
    # view와 연결할 html 파일
    template_name = 'projectapp/create.html'

    def form_valid( slef, form ):

        temp_project = form.save( commit=False )
        temp_project.save()

        return super().form_valid( form )
        pass # def form_valid 끝

    # 요청을 완료한후 보낼 url
    def get_success_url(self) -> str:
        return reverse( 'projectapp:detail', kwargs={ 'pk' : self.object.pk } )

    pass # class ProjectCreateView 끝


# 웹 요청 처리 클래스
# 게시글을 보여주는 클레스
class ProjectListView( ListView ):

    # 참조할 모델클레스
    model = Project
    # 템플릿에서 사용될 이름
    context_object_name = 'project_list'
    # 랜더링할 html 파일
    template_name = 'projectapp/list.html'
    # 한패이지에 보여줄 수
    paginate_by = 5

    pass # class ProjectListView 끝

# 41강 MultipleObjectMixin 에서 MultipleObjectMixin, def get_context_data 추가
# MultipleObjectMixin : 여러가지 오브젝트를 다룰수 있게 해준다
# 웹 요청 처리 클래스
class ProjectDetailView( DetailView, MultipleObjectMixin ):

    # 참조할 모델타입의 클레스
    model = Project
    # 탬플릿에서 사용될 이름을 정의
    context_object_name = 'target_project'
    # view와 연결할 탬플릿 html 파일
    template_name = 'projectapp/detail.html'

    # 보여주는 패이지수
    paginate_by = 25

    # 함수 오버라이트
    # 실질적으로 어떤 게시글을 가져올지 설정한다
    def get_context_data( self, **kwargs ):

        # project 값을 가져온다. 자신의 값
        project = self.object
        # user 값을 가져온다
        user = self.request.user

        # 로그인 했는지 안핬는지 확인
        if user.is_authenticated:
            # user와 project 값이 같은 값을 찾는다, 값이 없으면 안나옴
            subscription = Subscription.objects.filter( user=user, project=project )
            pass # if user.is_authenticated 끝
        # 45강 프로젝트 마무리 - 추가
        else: # 로그인 안했을때 처리
            subscription = None
            pass # else 끝

        # self.get_object()는 현재 상세 페이지의 프로젝트 객체를 반환한다.
        # 해당 프로젝트와 관련된 모든 Article 객체를 필터링한다.
        object_list = Article.objects.filter( project=self.get_object() )
        # 부모 클래스의 get_context_data를 호출하여 기본 컨텍스트 데이터를 가져온다.
        # 여기에 object_list와 subscription를 갱신하여 리턴한다.
        return super( ProjectDetailView, self ).get_context_data(
                     object_list=object_list, subscription=subscription, **kwargs )
        pass # def get_context_data 끝

    pass # class ProjectDetaileView 끝