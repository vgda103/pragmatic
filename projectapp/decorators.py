from django.http import HttpResponseForbidden
from projectapp.models import Project

def project_ownership_required( func ):

    def decorated( requst, *args, **kwargs ):

        # User.objects.get 에서 값을 받는대 kwargs[ 'pk' ]을 pk 에 넣어서 
        project = Project.objects.get( pk=kwargs[ 'pk' ] )
        # user 값과 request.user 같지 않다면
        if not project == requst.user:
            # 접근금지 주소로 재접속
            return HttpResponseForbidden()
            pass # if not project 끝

        return func( requst, *args, **kwargs )
        pass # def decorated 끝

    return decorated
    pass # def project_ownership_required 끝