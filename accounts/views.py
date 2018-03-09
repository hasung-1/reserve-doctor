from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import UserForm
from django.contrib.auth.models import User
#from .models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView,TemplateView
from .forms import HospitalSignUpForm, PersonalSignUpForm

# Create your views here.
class HospitalSignUpView(CreateView):
    
    model = User
    form_class = HospitalSignUpForm
    template_name = 'accounts/hospital_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hospital'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(addr_rest=form.data['addr_rest'])
        login(self.request, user)
        return redirect('/accounts/profile')
        

class PersonalSignUpView(CreateView):
    model = User
    form_class = PersonalSignUpForm
    template_name = 'accounts/personal_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'personal'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/profile')

class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
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

