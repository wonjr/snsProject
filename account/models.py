from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Photo(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
