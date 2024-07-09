from django.forms import ModelForm

from commentapp.models import Comment

# Comment 모델을 기반으로 한 폼 정의
class CommentCreationForm( ModelForm ):

    # ModelForm을 상속하면 django에 정보를 제공하는 Meta 클레스를 만들어야 한다.
    class Meta:

        # 참조할 객체
        model = Comment
        # 폼에서 사용할 모델의 필드들
        fields = [ 'content' ]

        pass # class Meta 끝

    pass # class CommentCreateForm 끝