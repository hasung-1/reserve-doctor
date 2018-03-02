from django import forms
#from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Hospital_User,Personal_User

class PersonalSignUpForm(UserCreationForm):
    #hospital_name = forms.CharField(max_length=100)
    
    sido = forms.CharField(max_length=30,widget=forms.HiddenInput(attrs={"id":"sido"}),required=False)
    gungu = forms.CharField(max_length=30,widget=forms.HiddenInput(attrs={"id":"gungu"}),required=False)
    dong = forms.CharField(max_length=30,widget=forms.HiddenInput(attrs={"id":"dong"}),required=False)
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self,commit=True):
        print("Save")
        user = super().save(commit=False)
        print(self.cleaned_data)
        user.user_type = 1
        user.save()
        #personal = Personal_User.objects.create(user=user)
        #student.interests.add(*self.cleaned_data.get('interests'))
        return user

class HospitalSignUpForm(UserCreationForm):
    #hospital_name = forms.CharField(max_length=100)
    
    sido = forms.CharField(max_length=30,widget=forms.HiddenInput(attrs={"id":"sido"}),required=False)
    gungu = forms.CharField(max_length=30,widget=forms.HiddenInput(attrs={"id":"gungu"}),required=False)
    dong = forms.CharField(max_length=30,widget=forms.HiddenInput(attrs={"id":"dong"}),required=False)
    
    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        print(self.cleaned_data)
        user.user_type = 2
        user.save()
        return user

#안씀
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','email','password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': '아이디',
            'email': '이메일',
            'password': '패스워드'
        }
    
    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15