from django.db import models

# Create your models here.

# DB의 내용을 만든다.
class Project( models.Model ):

    # 제목, 문자 필드 길이 20, null값 불가
    title = models.CharField( max_length=20, null=False )
    # 제목, 문자 필드 길이 200, null값 불가
    description = models.CharField( max_length=200, null=True )
    # 그림, 이미지필드 빈값 불가
    image = models.ImageField( upload_to='project', null=False )

    # 만든날자, 널값 허용
    create_at = models.DateField( auto_now_add=True )

    # 45강 프로젝트 마무리 - 추가
    # create창에서 project선택창에 게시글 번호와 게시글 이름 출력
    def __str__(self) -> str:
        return f'{ self.pk } : { self.title }'

    pass # class project 끝