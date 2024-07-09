from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreateionForm
from profileapp.models import Profile

# 웹 요청을 처리하는 클레스들
# TemplateView: 단순한 템플릿 렌더링.
# ListView: 모델 객체의 목록을 보여줌.
# DetailView: 모델 객체의 세부 정보를 보여줌.
# CreateView: 모델 객체를 생성하는 폼을 제공하고 처리.
# UpdateView: 모델 객체를 업데이트하는 폼을 제공하고 처리.
# DeleteView: 모델 객체를 삭제하는 기능을 제공
# Create your views here.

class ProfileCreateView( CreateView ):

    # 뷰에서 다룰 모델의 객체
    model = Profile
    # 템플릿에 전달될 컨텍스트의 변수명을 설정
    context_object_name = 'target_profile'
    # 사용할 폼의 클레스 객체
    form_class = ProfileCreateionForm
    # 33강. get_success_url - 삭제 -> 함수로 변경
    # 폼이 성공적으로 처리된후 이동시킬 주소
    # success_url = reverse_lazy( 'accountapp:hello_world' )
    # 템플릿 적용시킬 파일의 경로
    template_name = 'profileapp/create.html'

    # form에서 받는 데이터중 자신을 찾는다
    def form_valid( self, form ):

        # commit 옵션을 False로 하면 임시저장
        temp_profile = form.save( commit=False )
        # 현재 요청한 사용자를 프로필의 사용자로 설정
        temp_profile.user = self.request.user
        # 최종 저장
        temp_profile.save()

        # 부모의 form_valid의 리턴값을 리턴
        return super().form_valid( form )
    
    #  33강. get_success_url 추가
    # 재접속 패이지를 hello_world 에서 detail 로 바꾸는대 detail 에서는 pk 값을 받는다.
    # 클래스값을 직접적으로 보내기보단 함수로 접근하여 보낸다.
    # 메소드 오버로딩
    def get_success_url( self ):
        # kwargs 에 pk 이름의 딕셔너리타입에 self.object.user.pk 값을 넣어서 리턴
        return reverse( 'accountapp:detail', kwargs={ 'pk' : self.object.user.pk } )
        pass # def get_success_url 끝

    pass # class ProfileCreateView 끝

# 32강. 프로필 마무리
# 자기 자신의 프로필이 맞는지 확인과 다른 프로필에 대한 접근은 막는다
@method_decorator( profile_ownership_required, 'get' )
@method_decorator( profile_ownership_required, 'post' )
class ProfileUpdateView( UpdateView ):

    # 뷰에서 다룰 모델의 객체
    model = Profile
    # 템플릿에 전달될 컨텍스트의 변수명을 설정
    context_object_name = 'target_profile'
    # 사용할 폼의 클레스 객체
    form_class = ProfileCreateionForm
    # 33강. get_success_url 삭제
    # 폼이 성공적으로 처리된후 이동시킬 주소
    # success_url = reverse_lazy( 'accountapp:hello_world' )
    # 템플릿 적용시킬 파일의 경로
    template_name = 'profileapp/update.html'
    
    #  33강. get_success_url 추가
    # 재접속 패이지를 hello_world 에서 detail 로 바꾸는대 detail 에서는 pk 값을 받는다.
    # 클래스값을 직접적으로 보내기보단 함수로 접근하여 보낸다.
    # 메소드 오버로딩
    def get_success_url( self ):
        # kwargs 에 pk 이름의 딕셔너리타입에 self.object.user.pk 값을 넣어서 리턴
        return reverse( 'accountapp:detail', kwargs={ 'pk' : self.object.user.pk } )

    pass # class ProfileUpdateView 끝