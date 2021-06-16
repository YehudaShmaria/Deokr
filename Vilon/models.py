from django.db import models
from django.urls import reverse

  
# Create your models here.
class Curtain(models.Model):
    name = models.CharField(max_length=30,default='Vilon')
    YEAR_IN_SCHOOL_CHOICES = [
        ('tefira', 'תפירה'),
        ('zebra', 'זברה'),
        ('roma', 'רומאי'),
        ('van', 'ואניצני'),
    ]
    type = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES, max_length=30,default='tefira')
    title = models.TextField()
    descrption = models.TextField()
    img = models.ImageField(upload_to='static/images')

    def GetAbsoluteUrl(self):
        return reverse("detailes",kwargs={"id":self.id})
