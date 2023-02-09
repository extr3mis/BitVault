from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django import forms

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
    class Meta:
        model = User
        fields = ['username', 'email']

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = '/account/login/'
    template_name = "signup.html"

def landingView(request):
    return render(request, 'landing.html')

@login_required
def logoutView(request):
    logout(request)
    return redirect('/')