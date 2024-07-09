from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import Hello_World
from articleapp.models import Article

# 웹 요청을 처리하는 클레스들
# TemplateView: 단순한 템플릿 렌더링.
# ListView: 모델 객체의 목록을 보여줌.
# DetailView: 모델 객체의 세부 정보를 보여줌.
# CreateView: 모델 객체를 생성하는 폼을 제공하고 처리.
# UpdateView: 모델 객체를 업데이트하는 폼을 제공하고 처리.
# DeleteView: 모델 객체를 삭제하는 기능을 제공

# Create your views here.

# 28강 데코레이터 추가
has_ownership = [ account_ownership_required, login_required ]

# 인증 부분(로그인과 다시접속 부분)이 작성되어 있다, 클레스 안의 메서드에서는 사용불가
@login_required
def hello_world( request ):
    # 1강. 튜토리얼
    # return HttpResponse( '안녕하세요' )

    # 8강. include ,extends
    # return render( request, 'base.html' )

    # 9강 뼈대 만들기
    # return render( request, 'accountapp/hello_world.html' )

    # 28강 데코레이터에서 삭제
    # 27강 인증시스템
    # if request.user.is_authenticated:

    # 16강. post, get
    if request.method == 'POST':

        # 17강 post로 DB저장
        # 변수에 request.POST.get에서 hello_world_input이름의 데이터를 저장
        temp = request.POST.get( 'hello_world_input' )

        # 함수 객체를 변수에 저장
        new_hello_world = Hello_World()
        # new_hello_world.text에 temp 를 저장
        new_hello_world.text = temp
        # DB에 저장한다
        new_hello_world.save()

        # 18강 db접근 
        hello_world_list = Hello_World.objects.all()

        # 18강에서 new_hello_world 객체 helloworld_list 로 변경
        # 17-1강에서 'POST METHOD!!!' 객체 new_hello_world 로 변경
        # 17강에서 'POST METHOD!!!' 문자열을 변수로 변경 
        # # context : 데이터 꾸러미 같은것
        # return render( request, 'accountapp/hello_world.html',
        #             context={ 'hello_world_list' : hello_world_list } )

        # 18강 DB 접근
        # HttpResponseRedirect : 인자값으로 받은 주소로 다시 접속시켜준다
        # reverse : urls.py 에서 만들어진 값으로 주소를 만들어준다
        return HttpResponseRedirect( reverse( 'accountapp:hello_world' ) )
        pass # if request.method 끝
    else:
        # 기존
        # return render( request, 'accountapp/hello_world.html',
        #             context={ 'text' : 'Get METHOD!!!' } )

        # 18강 db 접근
        hello_world_list = Hello_World.objects.all()
        return render( request, 'accountapp/hello_world.html',
                    context={ 'hello_world_list' : hello_world_list } )        
        pass # else 끝
        # pass # request.user.is_authenticated 끝
        
    # 28강 데코레이터에서 삭제
    # 27강 인증시스템
    # else:
    #     # login 패이지로 다시 접속 시킨다
    #     return HttpResponseRedirect( reverse( 'accountapp:login' ) )
    #     pass # request.user.is_authenticated else 끝

    pass # def hello_word 끝
                         
class AccountCreateView( CreateView ):

    model = User # 유저 정보와 관련된 클래스
    form_class = UserCreationForm # 유저 폼에 관한 클레스
    # reverse_lazy와 reverse는 함수와 클레스를 호출하는 차이 때문에 분리된 것
    # 폼이 성공적으로 처리된 후에 보낼 URL
    success_url = reverse_lazy( 'accountapp:hello_world' )
    # 다른곳에서 이 변수명을 사용함으로 변수명 확인할것
    # 연결할 html 파일
    template_name = 'accountapp/create.html' 

    pass # class AccountCreateView 끝

# 41강 MultipleObjectMixin 에서 추가
# 24강. DeleteView
class AccounrtDetailView( DetailView, MultipleObjectMixin ):
    model = User
    # 24강 DetailView 추가
    # context_object_name 템플릿(html)에서 사용하는 이름을 다르게 설정한다.
    context_object_name = 'target_user'
    # 연결할 html 파일
    template_name = 'accountapp/detail.html'
    
    # 41강 MultipleObjectMixin 에서 추가
    # 한페이지에 보이는 수
    paginate_by = 25

    def get_context_data( self, **kwargs ):
        # self.get_object()는 현재 상세 페이지의 프로젝트 객체를 반환한다.
        # 해당 프로젝트와 관련된 모든 Article 객체를 필터링한다.
        object_list = Article.objects.filter( writer=self.get_object() )
        # 부모 클래스의 get_context_data를 호출하여 기본 컨텍스트 데이터를 가져온다.
        # 여기에 object_list를 추가하여 리턴한다.
        return super( AccounrtDetailView, self ).get_context_data(
                 object_list=object_list, **kwargs )
        pass # def get_context_data 끝


    # def get_context_data( self, **kwargs ):
    #     # self.get_object()는 현재 상세 페이지의 프로젝트 객체를 반환한다.
    #     # 해당 프로젝트와 관련된 모든 Article 객체를 필터링한다.
    #     object_list = Article.objects.filter( project=self.get_object() )
    #     # 부모 클래스의 get_context_data를 호출하여 기본 컨텍스트 데이터를 가져온다.
    #     # 여기에 object_list를 추가하여 리턴한다.
    #     return super( ProjectDetailView, self ).get_context_data(
    #                  object_list=object_list, **kwargs )




    pass # class AccounrtdetailView 끝

# 25강 UpdateView 
# 28강 Decorator  
# @method_decorator : 클레스에 데코레이터를 적용할때 사용,
# 인자값으로 데코레이션명과 사용할 메서드명
# @method_decorator( login_required, 'get' )
# @method_decorator( login_required, 'post' )
# @method_decorator( account_ownership_required, 'get' )
# @method_decorator( account_ownership_required, 'post' )
# 28강 데코레이터 수정
@method_decorator( has_ownership, 'get' )
@method_decorator( has_ownership, 'post' )
class AccountUpdateView( UpdateView ):

    model = User # 유저 정보와 관련된 클래스
    form_class = AccountUpdateForm # 유저 폼에 관한 클레스
    # context_object_name 템플릿(html)에서 사용하는 이름을 다르게 설정한다.
    context_object_name = 'target_user'
    # reverse_lazy와 reverse는 함수와 클레스를 호출하는 차이 때문에 분리된 것
    # 폼이 성공적으로 처리된 후에 보낼 URL
    success_url = reverse_lazy( 'accountapp:hello_world' )
    # 다른곳에서 이 변수명을 사용함으로 변수명 확인할것
    # 연결할 html 파일
    template_name = 'accountapp/update.html' 

    # # 28강 Decorator 에서 삭제
    # # 27강 인증시스템
    # # 부모 메소드를 오버라이딩
    # def get( self, *args, **kwargs ):

    #     # 실험 출력 테스트
    #     user01 = self.get_object()
    #     user02 = self.request.user
    #     print(f' user01 : {user01}, user02 : {user02}')  # 디버깅 출력

    #     # 유저의 정보가 있다면 그리고 self.get_object() 와 self.request.user이 같은면
    #     # self.get_object()는 urls.py 에서 요구하는 update/<int:pk> 에서 pk 값
    #     if self.request.user.is_authenticated and user01 == user02:
    #         # 부모의 get 메소드값을 리턴
    #         return super().get( *args, **kwargs )
    #         pass # self.request.user.is_authenticated 끝
    #     else: # 유저의 정보가 없다면
    #         # 금지된 곳에 접근 했다는 패이지 값을 리턴
    #         return HttpResponseForbidden()
    #         # 로그인 페이지로 접속시킨다. 기존값
    #         # return HttpResponseRedirect( reverse( 'accountapp:login' ) )
    #         pass # self.request.user.is_authenticated else 끝

    #     pass # def get 끝
    
    # # 27강 인증시스템
    # # 부모 메소드를 오버라이딩
    # def post( self, *args, **kwargs ):

    #     user01 = self.get_object()
    #     user02 = self.request.user
    #     print(f' user01 : {user01}, user02 : {user02}')  # 디버깅 출력

    #     # 유저의 정보가 있다면 그리고 self.get_object() 와 self.request.user이 같은면
    #     # self.get_object()는 urls.py 에서 요구하는 update/<int:pk> 에서 pk 값
    #     if self.request.user.is_authenticated and user01 == user02:
    #         # 부모의 get 메소드값을 리턴
    #         return super().post( *args, **kwargs )
    #         pass # self.request.user.is_authenticated 끝
    #     else: # 유저의 정보가 없다면
    #         # 금지된 곳에 접근 했다는 패이지 값을 리턴
    #         return HttpResponseForbidden()
    #         # 로그인 페이지로 접속시킨다. 기존값
    #         # return HttpResponseRedirect( reverse( 'accountapp:login' ) )
    #         pass # self.request.user.is_authenticated else 끝

    #     pass # def post 끝

    pass # class AccountUpdateView 끝

# 26강 DeleteView
# 28강 Decorator  
# @method_decorator : 클레스에 데코레이터를 적용할때 사용,
# 인자값으로 데코레이션명과 사용할 메서드명
# @method_decorator( login_required, 'get' )
# @method_decorator( login_required, 'post' )
# @method_decorator( account_ownership_required, 'get' )
# @method_decorator( account_ownership_required, 'post' )
# 28강 데코레이터 수정
@method_decorator( has_ownership, 'get' )
@method_decorator( has_ownership, 'post' )
class AccountappDeleteView( DeleteView ):
    model = User # 유저 정보 관련 클레스
    # 폼이 성공적으로 처리된 후 보낼 주소
    # context_object_name 템플릿(html)에서 사용하는 이름을 다르게 설정한다.
    context_object_name = 'target_user'
    success_url = reverse_lazy( 'accountapp:login' )
    # 연결할 html 파일
    template_name = 'accountapp/delete.html'

    # # 28강 Decorator 에서 삭제
    # # 27강 인증시스템
    # # 부모 메소드를 오버라이딩
    # def get( self, *args, **kwargs ):

    #     # 유저의 정보가 있다면 그리고 self.get_object() 와 self.request.user이 같은면
    #     # self.get_object()는 urls.py 에서 요구하는 update/<int:pk> 에서 pk 값
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         # 부모의 get 메소드값을 리턴
    #         return super().get( *args, **kwargs )
    #         pass # self.request.user.is_authenticated 끝
    #     else: # 유저의 정보가 없다면
    #         # 금지된 곳에 접근 했다는 패이지 값을 리턴
    #         return HttpResponseForbidden()
    #         # 로그인 페이지로 접속시킨다. 기존값
    #         # return HttpResponseRedirect( reverse( 'accountapp:login' ) )
    #         pass # self.request.user.is_authenticated else 끝

    #     pass # def get 끝

    # # 28강 Decorator 에서 삭제
    # # 27강 인증시스템
    # # 부모 메소드를 오버라이딩
    # def post( self, *args, **kwargs ):

    #     # 유저의 정보가 있다면 그리고 self.get_object() 와 self.request.user이 같은면
    #     # self.get_object()는 urls.py 에서 요구하는 update/<int:pk> 에서 pk 값
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post( *args, **kwargs )
    #         pass # self.request.user.is_authenticated 끝
    #     else: # 유저의 정보가 없다면
    #         # 금지된 곳에 접근 했다는 패이지 값을 리턴
    #         return HttpResponseForbidden()
    #         # 로그인 페이지로 접속시킨다. 기존값
    #         # return HttpResponseRedirect( reverse( 'accountapp:login' ) )
    #         pass # self.request.user.is_authenticated else 끝

    #     pass # def post 끝

    pass # class AccountappDeleteView 끝