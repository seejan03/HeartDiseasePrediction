from django.contrib.auth.models import User
from django.shortcuts import redirect

def simple_middleware(get_response):
    def middleware(request):


            print(request.session.get('user_id'))
            print(request)
            returnUrl = request.META['PATH_INFO']
            print(request.META['PATH_INFO'])
            if not request.session.get('user_id'):
                return redirect(f'login?return_url={returnUrl}')

            response = get_response(request)
            return response

    return middleware