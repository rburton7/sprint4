from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from account.views.forms import LoginForm
from django import forms
from django.http import HttpResponseRedirect


@view_function
def process_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
       
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
       
       
           

    else:
        form = LoginForm()

    context = {
       'form':form,
    }
    return request.dmp.render('login.html', context)


