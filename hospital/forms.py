from django import forms
from .models import Reserve,Time
from django.contrib.admin import widgets
#from datetime import date,time
from django.utils import timezone
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm,Select

class ReserveForm(ModelForm):
    def __init__(self, hospital, *args, **kwargs):
        super().__init__(*args,**kwargs)

        #처음에는 null로 세팅
        #self.fields['time'].queryset = Time.objects.none()
        
    class Meta:
        model = Reserve
        fields= ['date','time']
        

        dateOptions = {
            'format': 'yyyy-mm-dd',
            'autoclose': True,
            'todayHighlight' : True
            }
        
        #widgets={'date':DateWidget(attrs={'id':"datepicker"}, usel10n = True, bootstrap_version=3,options=dateOptions)}
        widgets= {
                'date':DateWidget(attrs={'id':"datepicker"}, bootstrap_version=3,options=dateOptions),
                #'time':Select(attrs={'id':'time_select'}),
            }
        
        