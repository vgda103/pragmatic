from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 데이터 구조를 정의 한다
class Profile( models.Model ):

    # 30. 프로파일시작_모델폼
    # models.OneToOneField : 객체와 객체를 1:1로 연결, 첫번째 인자값 User 연결한다.
    # 첫번째 인자 : 연결할 객체, on_delete : 연결될 객체게 지워질때 적용할 값의 옵션,
    #  related_name : profile의 네임스페이스 같은거 profile에 바로 접근하게 해준다.
    # models.CASCADE : 객체가 지워질때 같이 지워지는 옵션값
    # user 는 서버에서 처리하는 변수
    user = models.OneToOneField( User, on_delete=models.CASCADE, related_name='profile' )

    # models.ImageField : 사진을 관리하는 객체, 
    # upload_to : 이미지를 받아서 서버 어디에 저장될지 정하는 경로,
    # 기본적인 경로는 MEDIA_ROOT 에서 정해저 있고 그 하위 폴더를 명칭
    image = models.ImageField( upload_to='profile/', null=True )
    # models.CharField : 문자열, max_length : 문자열 최대길이, unique:유일설정, null 허용
    # unique : models.CharField 객체중 유일해야 한다.
    nickname = models.CharField( max_length=20, unique=True, null=True )
    # models.CharField : 문자열, max_length : 문자열 최대길이, null 허용
    message = models.CharField( max_length=100, null=True )

    pass # class Profile 끝
