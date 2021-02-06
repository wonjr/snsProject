from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=200)

    def __str__(self):#_=>이미 내장된 함수,private로 작동
        return self.text