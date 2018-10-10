from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView)
from django.contrib.auth import logout
from django.contrib.auth.decorators import  login_required
from social_site import forms


# Create your views here.
class SignUp(CreateView):
    form_class=forms.UserSignUpForm
    success_url=reverse_lazy('login')
    template_name='social_site/signup.html'

@login_required
def logout_view(request):
    logout(request)
    return redirect(request,'home')

