from django.db import models
from django.conf import settings
# Create your models here.
class Hospital(models.Model):
    name=models.CharField(max_length=100)
    tel=models.CharField(max_length=20)
    addr=models.CharField(max_length=100)
    #doctor=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Time(models.Model):
    hospital = models.ForeignKey(Hospital)
    time = models.TimeField()
    class Meta:
        ordering=["time"]

    def __str__(self):
        return str(self.time)


class Reserve(models.Model):
    hospital = models.ForeignKey(Hospital)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateField()
    time = models.ForeignKey(Time)
    #item_set = models.ManyToManyField(Time)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #이 세개의 칼럼은 유니크해야함
        unique_together=('hospital','date','time',)