from django.contrib.auth import authenticate, login
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpRequest


def logging_in_service( request, **kwargs):
        username=kwargs.get('username')
        password=kwargs.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True
            # Redirect to a success page.
            ...
        else:
            return False
            # Return an 'invalid login' error message.
            ...