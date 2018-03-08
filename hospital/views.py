from django.core import serializers
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ReserveForm
from django.http import HttpResponse
import json
import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import DetailView,ListView
from django.core.exceptions import ValidationError

class HospitalDV(DetailView):
    """
	DetailView 디폴트 지정 속성
	1) 컨텍스트 변수 : object (URLConf 에서 pk 파라미터 값을 활용하여 DB 레코드 조회)
	2) 템플릿 파일 : (모델명소문자_detail.html)
	"""
    model = Hospital

class HospitalLV(ListView):
    model = Hospital
    paginate_by = 10

'''
    def get_context_data(self,**kwargs):
        context = super(HospitalLV,self).get_context_data(**kwargs)
        subject = self.request.GET.get('subject')
        search_text = self.request.GET.get('search_text')
        
        qs = Hospital.objects.all()
        lst = []
        for hospital in qs:
            dic = {}
            dic["id"] = hospital.id
            dic["name"] = hospital.name
            dic["tel"] = hospital.tel
            dic["addr"] = hospital.addr
            dic["subjects"] = hospital.GetSubjects()
            lst.append(dic)
        
        context.update(
            {
                'hospital_list':lst,
                'subject_list':Subject.objects.all(),
                'sido_list':Sido.objects.values('sidoCode','sidoName').distinct(),
            }
        )
        
        return context
        '''
'''
    def get_queryset(self):
        print("get_queryset")
        print(self.kwargs)
        qs = self.model.objects.all()

        try:
            subject = self.kwargs['subject']
            search_text = self.kwargs['search_text']
            print(subject)
        except:
            subject=''
            search_text = ''
        if(search_text!=''):
            qs = qs.filter(name__icontains=search_text,subjects=subject)
        
        return qs
'''
class ReserveLV(ListView):
    model = Reserve

    def get_queryset(self):
        queryset = super(ReserveLV, self).get_queryset()
        
        #병원
        if(self.request.user.user_type==2):
            pass

        #환자, Admin 포함
        else:
            pass
        

        queryset = queryset.filter(user=self.request.user)
        return queryset


# Create your views here.
def hospital_list(request):
    qs = Hospital.objects.all()
    subject = request.GET.get('subject')
    search_text = request.GET.get('search_text')

    if search_text:
        qs = qs.filter(name__icontains=search_text,subjects=subject)

    lst = []
    for hospital in qs:
        dic = {}
        dic["id"] = hospital.id
        dic["name"] = hospital.name
        dic["tel"] = hospital.tel
        dic["addr"] = hospital.addr
        dic["subjects"] = hospital.GetSubjects()
        lst.append(dic)

    #페이지 처리
    paginator = Paginator(lst,10)#20개 보여주기

    page = request.GET.get('page')

    try:
        hospitals = paginator.page(page)
    except PageNotAnInteger:
        hospitals = paginator.page(1)
    except EmptyPage:
        hospitals = paginator.page(paginator.num_pages)

    return render(request,'hospital/hospital_list.html',{
        'hospital_list':hospitals,
        'subject_list':Subject.objects.all(),
        #나중에는 sido만 나가게 변경할것
        'sido_list':Sido.objects.values('sidoCode','sidoName').distinct(),
        
    })



@login_required
def reserve_new(request,hospital_id):
    hospital = get_object_or_404(Hospital,id = hospital_id)
    if request.method=="POST":
        print(request.POST)
        form = ReserveForm(hospital,request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)

            #form fields 땜에 validation 체크를 여기서
            '''
            if Reserve.objects.filter(hospital=hospital_id, doctor=form.cleaned_data['doctor'],
                time=form.cleaned_data['time'],date=form.cleaned_data['date']).exists():
                raise ValidationError('Solution with this Name already exists for this problem')
            '''
            print("after cleaned_data")            
            #다시
            # 동영상 볼것
            
            reserve = form.save(commit=False)
            reserve.user = request.user
            reserve.hospital = hospital
            reserve.save()
            form.save_m2m()
            
            return redirect('hospital:reserve_list')
        else:
            print("not valid!!!!!!!!!")
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
@require_POST
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

@require_POST
def selectSido(request):
    sidoCode = request.POST.get('sidoCode',None)
    gunguList = list(Sido.objects.filter(sidoCode=sidoCode).values_list('gunguCode','gunguName'))
    gunguJson = json.dumps(gunguList)
    context={
        'data':gunguJson,
    }
    return HttpResponse(json.dumps(context))

def cancelReserve(request):
    print(request.POST)
    reserve_id = request.POST.get('reserve_id',None)
    row = Reserve.objects.get(id=reserve_id)
    row.delete()
    return render(request,'hospital/reserve_list.html')

def reserve(request):
    hospital_id = request.POST.get('hospital_id',None)
    hospital = get_object_or_404(Hospital,id = hospital_id)
    
    #Ajax 일때만 온다.현재는
    if request.method=="POST":
        form = ReserveForm(hospital,request.POST)
        if form.is_valid():
            print("valid")
            #다시 동영상 볼것 -- cleaned_data 에 대해서 알아볼것0303
            print(form.cleaned_data)
            if Reserve.objects.filter(hospital=form.cleaned_data['hospital_id'], doctor=form.cleaned_data['doctor'],
                time=form.cleaned_data['time'],date=form.cleaned_data['date']).exists():
                raise ValidationError('Solution with this Name already exists for this problem')
            '''
            reserve = form.save(commit=False)
            reserve.user = request.user
            reserve.hospital = hospital
            reserve.save()
            form.save_m2m()
            '''
            context={
                'status':1,
                'message':'OK'
            }
            return HttpResponse(json.dumps(context))
        else:
            context={
                'status':1,
                'message':form.errors
            }
            print("=================================")
            print(form.errors)
            print("=================================")
            return HttpResponse(json.dumps(context))
    else:
        form = ReserveForm(hospital)
    
    return render(request,'hospital/reserve_form.html',{
            'form':form,
            'hospital_info':hospital,
    })
    