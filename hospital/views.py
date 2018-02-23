from django.core import serializers
from django.shortcuts import render,get_object_or_404,redirect
from .models import Hospital,Reserve,Time
from django.contrib.auth.decorators import login_required
from .forms import ReserveForm
from django.views.generic import ListView
from django.http import HttpResponse
import json
import datetime

# Create your views here.
def index(request):
    return render(request,'hospital/index.html',{
        'hospital_list':Hospital.objects.all(),
    })

@login_required
def reserve_new(request,hospital_id):
    hospital = get_object_or_404(Hospital,id = hospital_id)
    
    if request.method=="POST":
        print(request.POST)
        form = ReserveForm(hospital,request.POST)
        
        if form.is_valid():
            #다시 동영상 볼것
            reserve = form.save(commit=False)
            reserve.user = request.user
            reserve.hospital = hospital
            reserve.save()
            form.save_m2m()
            return redirect('hospital:index')
    else:
        form = ReserveForm(hospital)

    return render(request,'hospital/reserve_form.html',{
            'form':form,
            'hospital_info':hospital,
    })

#시간을 문자열로
def timeConvertor(o):
    if isinstance(o, datetime.time):
        return o.__str__()

#Ajax
def selectDate(request):
    hospital_id=request.POST.get('hospital_id',None)
    reserve_date=request.POST.get('reserve_date',None)
    doctor_id = request.POST.get('doctor_id',None)

    #예약되어있는 리스트
    reserved_list = Time.objects.filter(hospital_id=hospital_id,reserve__date=reserve_date,reserve__doctor_id=doctor_id).values('time')
    exclude_list = Time.objects.filter(hospital_id=hospital_id).exclude(time__in=reserved_list).values_list('id','time')
    qs_json = json.dumps(list(exclude_list),default=timeConvertor)
    context = {
        'data':qs_json,
        }
    
    return HttpResponse(json.dumps(context))