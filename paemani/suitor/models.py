from django.db import models
from .choices import *

class Suitor(models.Model):
#    suitor_id = models.AutoField()
    name=models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    gender=models.BooleanField(default=True)
    email=models.EmailField(max_length=128)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    age = models.PositiveSmallIntegerField(default=0)
    registration_date = models.DateTimeField(auto_now=True)
#    avatar = models.ImageField(default=None,required=False)

    def __unicode__(self):
        return "%s %s" %(self.name,self.last_name)

    def __str__(self):
        return "%s %s" %(self.name,self.last_name)



class Aprnc (models.Model):
    suitor_id= models.ForeignKey('Suitor', on_delete=models.CASCADE,default=None)
    ethnicity = models.CharField(max_length=10, choices=ETHNICITY_CHOICES, default='white')
    hair_color = models.CharField(max_length=6, choices=HAIR_COLOR_CHOICES, default='black')
    height = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __unicode__(self):
        return "Ethnicity - %s, Hair - %s, Width -%d, Weight -%f" %(self.ethnicity, self.hair_color, self.width, self.weight)

    def __str__(self):
        return "Ethnicity - %s, Hair - %s, Width -%d, Weight -%f" %(self.ethnicity, self.hair_color, self.width, self.weight)
