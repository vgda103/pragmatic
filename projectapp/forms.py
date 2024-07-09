from django.forms import ModelForm

from projectapp.models import Project


# Project 모델을 기반으로 한 폼 정의
class ProjectCreainoneForm( ModelForm ):

    # ModelForm을 상속하면 django에 정보를 제공하는 Meta 클레스를 만들어야 한다.
    class Meta:

        # 폼이 참조할 모델
        model = Project
        # 폼에서 사용할 모델의 필드들
        fields = [ 'title', 'description', 'image',  ]

        pass # class Mete 끝


    pass # class CreateProjectForm 끝