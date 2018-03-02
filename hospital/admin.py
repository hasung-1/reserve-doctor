from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name','tel','addr')


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('hospital','time')

@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('hospital','user','time')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject',)

@admin.register(Sido)
class SidoAdmin(admin.ModelAdmin):
    list_display = ('sidoCode','sidoName','gunguCode','gunguName',)