from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login

from . import forms

def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(
        request,
        'user/signup.html',
        context={
            'form': form
        }
    )
