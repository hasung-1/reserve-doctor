from django.conf.urls import url
from . import views
from .views import HospitalDV,ReserveLV



urlpatterns=[
    url(r'^$',views.hospital_list,name='hospital_list'),
    #url(r'^$',views.HospitalLV.as_view(),name='hospital_list'),
    url(r'(?P<hospital_id>\d+)/new/$', views.reserve_new, name='reserve_new'),
    url(r'reserve_list$', ReserveLV.as_view(), name='reserve_list'),
    url(r'(?P<pk>\d+)/$', HospitalDV.as_view(), name='detail'),
    #url(r'^$',views.hospital_reserve_list,name='hospital_reserve_list'),


    ##Ajax
    url(r'^selectdate/$',views.selectDate,name="select_date"),
    url(r'^selectSido/$',views.selectSido,name="select_sido"),
    url(r'^reserve_cancel/$',views.cancelReserve,name="reserve_cancel"),
    #url(r'^reserve/$',views.reserve,name="reserve"),
]