from django import forms
#from django.contrib.auth.models import User
from .models import User,Hospital_User,Personal_User
from hospital.models import Hospital, Sido, Subject
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction



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
    
    sido = forms.CharField(
        max_length=20,
        widget=forms.HiddenInput(attrs={"id":"sido"}),
        required=False)
    gungu = forms.CharField(
        max_length=20,
        widget=forms.HiddenInput(attrs={"id":"gungu"}),
        required=False)
    dong = forms.CharField(
        max_length=20,
        widget=forms.HiddenInput(attrs={"id":"dong"}),
        required=False)
    addr = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput(attrs={"id":"addr"}),
        required=False)
    addr_rest = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput(attrs={"id":"addr_rest"}),
        required=False)
    tel = forms.CharField(max_length=13)
    subjects = forms.ModelMultipleChoiceField(
        queryset = Subject.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required =True
        )
    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self,commit=True, *args, **kvargs):
        #User 저장
        user = super().save(commit=False)
        print(self.cleaned_data)
        user.user_type = 2
        user.save()

        #주소로 검색으로 sido 인자 id값 전달
        si_gu = Sido.objects.get(
            sidoName__icontains=self.cleaned_data['sido'],
            gunguName=self.cleaned_data['gungu'])
        si_gu.save()
        #Hospital_user 저장
        hospital_user = Hospital_User.objects.create(user=user)
        hospital_user.save()

        
        real_addr = self.cleaned_data['addr'] + " " + self.cleaned_data['addr_rest']
        
        #Hospital 저장
        hos=Hospital()
        hos = Hospital.objects.create(
            name='name',
            sidogungu = si_gu,
            dong=self.cleaned_data['dong'],
            tel=self.cleaned_data['tel'],
            addr=real_addr)
        hos.save()
        hos.subjects.add(*self.cleaned_data.get('subjects'))
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