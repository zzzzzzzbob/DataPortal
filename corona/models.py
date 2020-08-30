from django.db import models
from djongo import models as jm

# Create your models here.

class coronaData(models.Model):
    _id = jm.ObjectIdField()
    today = models.IntegerField()

    def __str__(self):
    	return "저장한 숫자는 :"+str(self.today)

    class Meta:
        managed = False
        db_table = 'coronaData'
        verbose_name_plural = "테스트"
