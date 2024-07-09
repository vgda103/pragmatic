from django.http import HttpResponseForbidden

from profileapp.models import Profile

def profile_ownership_required( func ):

    def decorated( request, *args, **kwargs ):

        # User.objects.get 에서 값을 받는대 kwargs[ 'pk' ]을 pk 에 넣어서 
        profile = Profile.objects.get( pk=kwargs[ 'pk' ] )
        # user 값과 request.user 같지 않다면
        if not profile.user == request.user:
            # 접근금지 주소로 재접속
            return HttpResponseForbidden()
            pass # if not user 끝

        # func에 request, *args, **kwargs의 값을 넣어 나오는 값을 리턴
        return func( request, *args, **kwargs )
        pass # def decorated 끝

    return decorated
    pass # def decorator 끝