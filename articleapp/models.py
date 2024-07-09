from django.db import models
from django.contrib.auth.models import User

from projectapp.models import Project

# Create your models here.

# DB 테이블 구조 만들기
class Article( models.Model ):

    # User 모델에 대한 ForeignKey를 가져온다.
    # on_delete : 작성자가 탈퇴했을 때 게시물은 남고, 작성자는 알 수 없도록 설정한다.
    # related_name : 네임스페이스, User 객체에서 Article을 접근할 때 사용할 이름.
    writer = models.ForeignKey( User, on_delete=models.SET_NULL,
                                related_name='article', null=True )
    # project 모델에 대한 ForeignKey를 가져온다.    
    project = models.ForeignKey( Project, on_delete=models.SET_NULL,
                                related_name='article', null=True )

    # 200자 길이의 문자열 필드 생성, null 값 사용
    title = models.CharField( max_length=200, null=True )
    # 이미지 필드, 이미지를 저장할 폴더 경로를 지정, null 값을 허용하지 않음.
    image = models.ImageField( upload_to='article/', null=False )
    # 문자열 상위 필드 생성, null 값 사용
    content = models.TextField( null=True )

    # 게시물 생성 날짜를 자동으로 추가, null 값을 허용.
    create_at = models.DateField( auto_now_add=True, null=True )
    pass # class Article 끝