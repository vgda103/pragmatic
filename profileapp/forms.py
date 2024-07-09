from django.forms import ModelForm

from profileapp.models import Profile

# 30강. 프로파일, 모델폼 
# 클레스 생성 및 상속
class ProfileCreateionForm( ModelForm ):
    
    # 클레스 생성, django에 정보를 제공하는 클레스, 꼭 Mata 라고 명시해야함
    class Meta:
        
        # 클레스 맴버 정의 및 생성
        model = Profile
        # 명칭을 정의
        # 이미지를 바꿀때 image를 누구것인지를 모름, 하지만 서버에서 바꾸기로함
        fields = [ 'image', 'nickname', 'message' ]

        pass # class Meta 끝

    pass # class ProfileCreateionForm 끝