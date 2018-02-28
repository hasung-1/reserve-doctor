from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import UserForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView,TemplateView


# Create your views here.

class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_suer = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            return redirect(settings.LOGIN_URL)
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })

@login_required
def profile(request):
    return render(request,'accounts/profile.html')

