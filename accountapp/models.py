from django.db import models

# Create your models here.

# 14강 모델, DB연동
# 데이터 구조를 정의 한다
class Hello_World( models.Model ):
    # models.CharField : 문자열, max_length : 문자열 최대길이
    text = models.CharField( max_length=255, null=False )
    pass # class Hello_World 끝