from django.db import models
from django.conf import settings

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=50)
    def __str__(self):
        return str(self.subject)

class Hospital(models.Model):
    name=models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)
    tel=models.CharField(max_length=20)
    addr=models.CharField(max_length=100)
    
    
    def GetSubjects(self):
        return list(Hospital.objects.first().subjects.all().values_list('subject',flat=True))
        

    def __str__(self):
        return self.name

class Time(models.Model):
    hospital = models.ForeignKey(Hospital)
    time = models.TimeField()
    class Meta:
        ordering=["time"]

    def __str__(self):
        return str(self.time)

class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)

class Reserve(models.Model):
    hospital = models.ForeignKey(Hospital)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()
    time = models.ForeignKey(Time)
    doctor = models.ForeignKey(Doctor,null=True)

    #item_set = models.ManyToManyField(Time)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #이 세개의 칼럼은 유니크해야함
        unique_together=('hospital','doctor','date','time',)

        verbose_name = "예약내역"

        #정렬
        ordering=['-date','-time']

class Sido(models.Model):
    sidoCode = models.CharField(max_length=2)
    sidoName = models.CharField(max_length=20)

    gunguCode = models.CharField(max_length=5)
    gunguName = models.CharField(max_length=20)