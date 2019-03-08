from django import forms
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        #authenticate the user to check for the valid creds
        self.user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Username or Password is Incorrect')
        return self.cleaned_data

    # def commit(self):
    #     login(self.request, self.user)