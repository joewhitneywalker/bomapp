from django.db import models

# Create your models here.

class Bom(models.Model):
    
    style_name= models.CharField(max_length=200)
    style_number= models.CharField(max_length=5)
    created_by = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    season = models.CharField(max_length=4, default='FA20', editable=True)#MAIN SQL QUERY
    category = models.CharField(max_length=25, default='OUTERWEAR', editable=True)
    colorway = models.CharField(max_length=25)
    img = models.CharField(max_length=250)

def __str__(self):
        return self.style_name
class Meta:
        ordering = ['style_number']


    