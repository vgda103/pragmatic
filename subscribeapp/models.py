from django.db import models
from django.contrib.auth.models import User

from projectapp.models import Project

# Create your models here.

class Subscription( models.Model ):

    # User 모델에 대한 ForeignKey를 가져온다.
    # on_delete : 작성자가 탈퇴했을 때 모두 삭제
    # related_name : 네임스페이스, User 객체에서 Subscription의 User을 접근할 때 사용할 이름.
    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name='subscription' )
    # project 모델에 대한 ForeignKey를 가져온다.
    # on_delete : 작성자가 탈퇴했을 때 모두 삭제
    # related_name : 네임스페이스, User 객체에서 Subscription의 Project을 접근할 때 사용할 이름.
    project = models.ForeignKey( 
                Project, on_delete=models.CASCADE, related_name='subscription' )
    
    # Meta 클래스는 Django 모델의 옵션을 설정할 때 사용됩니다.
    class Meta:
        # user가 하나의 project 한번만 가능하게 쌍으로 연결
        unique_together = ( 'user', 'project' )

    pass # class Subscription 끝