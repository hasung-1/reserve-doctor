from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'(?P<hospital_id>\d+)/new/$', views.reserve_new, name='reserve_new'),


    ##Ajax
    url(r'^selectdate/$',views.selectDate,name="select_date"),
]