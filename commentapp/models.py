from django.db import models
from django.contrib.auth.models import User

from articleapp.models import Article

# Create your models here.

class Comment( models.Model ):
    
    # Article 모델에 대한 ForeignKey를 가져온다.
    # on_delete : 작성자가 탈퇴했을 때 게시물은 남고, 작성자는 알 수 없도록 설정한다.
    # related_name : 네임스페이스, Article 객체에서 Article을 접근할 때 사용할 이름.
    # Article 정보를 접근할 객체, 게시물을 나타내는 Article 모델에 대한 외래 키
    article = models.ForeignKey( Article, on_delete=models.SET_NULL,
                               null=True, related_name='comment' )
    # User 정보를 접근할 객체, 댓글 작성자를 나타내는 User 모델에 대한 외래 키
    writer = models.ForeignKey( User, on_delete=models.SET_NULL, 
                               null=True, related_name='comment' )
    
    # 문자열필드 보다 많이 사용할수 있는 필드
    content = models.TextField( null=False )

    # 생성시간을 저장한다
    created_at = models.DateTimeField( auto_now_add=True ) 

    pass # class Comment 끝