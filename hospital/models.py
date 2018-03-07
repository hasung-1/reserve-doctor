from django.db import models
from django.conf import settings

# Create your models here.
class Subject(models.Model):
    code = models.CharField(max_length=3)
    subject = models.CharField(max_length=50)
    class Meta:
        #정렬
        ordering=['code',]

    def __str__(self):
        return str(self.subject)

class Sido(models.Model):
    sidoCode = models.CharField(max_length=6)
    sidoName = models.CharField(max_length=20)

    gunguCode = models.CharField(max_length=6)
    gunguName = models.CharField(max_length=20)

    def __str__(self):
        return self.sidoName + " " + self.gunguName

class Hospital(models.Model):
    name=models.CharField(max_length=150)
    subjects = models.ManyToManyField(Subject)
    sidogungu = models.ForeignKey(Sido)
    dong = models.CharField(max_length=150)
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

        #verbose_name = "예약내역"

        #정렬
        ordering=['-date','-time']



    