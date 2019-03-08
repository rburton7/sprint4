from django.contrib.auth import logout
from account.models import User
from django_mako_plus import view_function
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    logout(request)

    return HttpResponseRedirect('/')