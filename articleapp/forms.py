from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project

# Article 모델을 기반으로 한 폼 정의
class ArticleCreationForm( ModelForm ):

    # 43강 WYSIWYG - 추가
    # forms.CharField를 커스터마이징하기 위해 widget을 설정한다
    # widget으로 forms.Textarea를 사용하고, 클래스와 스타일 속성을 미리 정의한다
    content = forms.CharField( widget=forms.Textarea( attrs={ 
                        'class' : 'editable text-start',
                        'style' : 'height: auto;' } ) )
    
    # 43강 WYSIWYG - 추가
    # forms.ModelChoiceField를 커스터마이징하기 위해 queryset과 required 속성을 설정한다
    # queryset : 선택 목록, Project.objects.all()을 사용해 모든 프로젝트를 가져온다
    # required : 선택 필수 여부, True이면 반드시 선택해야 하고, False이면 선택하지 않아도 된다
    project = forms.ModelChoiceField( queryset=Project.objects.all(), required=False )

    # ModelForm을 상속하면 django에 정보를 제공하는 Meta 클레스를 만들어야 한다.
    class Meta:

        # 폼이 참조할 모델
        model = Article
        # 41강 MultipleObjectMixin 에서 project 추가
        # 폼에서 사용할 모델의 필드들
        fields = [ 'title', 'image', 'project', 'content' ]
        
        pass # 끝

    pass # class ArticleCreationForm 끝