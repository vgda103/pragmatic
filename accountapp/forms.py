from typing import Any
from django.contrib.auth.forms import UserCreationForm

# UserCreationForm 상속 받아서 클레스 생성
class AccountUpdateForm( UserCreationForm ):

    # 생성자
    def __init__(self, *args, **kwargs) -> None:
        # 부모 생성자 호출
        super().__init__(*args, **kwargs)

        # 맴버 변수중 fields의 딕셔너리 타입의 username 이름에  disabled 값을 바꾼다
        self.fields[ 'username' ].disabled = True
        pass # def __init__ 끝

    pass # class AccountUpdateForm 끝