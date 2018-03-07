from django import forms
from .models import Reserve,Time,Doctor,Hospital
from django.contrib.admin import widgets
#from datetime import date,time
from django.utils import timezone
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm,Select
from django.core.exceptions import NON_FIELD_ERRORS

class ReserveForm(ModelForm):
    def __init__(self, hospital, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        #처음에는 null로 세팅
        #hospital_id=self.data['hospital_id']
        #reserve_date = self.data['date']

        #doctor_id = self.data['doctor_id']
        
        '''
        if self.data:
            print(self.data)
            hospital_id = hospital.id
            #hospital_id=self.data['hospital_id']
            reserve_date = self.data['date']

            reserved_list = Time.objects.filter(hospital_id=hospital_id,reserve__date=reserve_date,reserve__doctor_id=doctor_id).values('time')
            self.fields['time'].queryset = exclude_list = Time.objects.filter(hospital_id=hospital_id).exclude(time__in=reserved_list).values_list('time')
        '''
        #의사 목록
        self.fields['doctor'].queryset = Doctor.objects.filter(hospital=hospital)
        self.fields['doctor'].empty_label = None
        
        #self.fields['hospital'].queryset = Hospital.objects.filter(id = hospital.id)
        #self.fields['hospital'].empty_label = None

        print(self.fields['hospital'].queryset)
    class Meta:
        model = Reserve
        fields= ['hospital','doctor','date','time']
        
        #NON_FIELD_ERROR 오버라이드
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "얘약 시간이 없습니다.",
            }
        }


        #예약을 언제 까지 받을지 결정해야함(startDate,endDate)
        dateOptions = {
            'format': 'yyyy-mm-dd',
            'autoclose': True,
            'todayHighlight' : True,
            'startDate':'+1d',
            'endDate':'+7d',
            }
        
        #widgets={'date':DateWidget(attrs={'id':"datepicker"}, usel10n = True, bootstrap_version=3,options=dateOptions)}
        widgets= {
                'date':DateWidget(attrs={'id':"datepicker"}, bootstrap_version=3,options=dateOptions),
                'hospital':forms.HiddenInput(),
            }
        
        