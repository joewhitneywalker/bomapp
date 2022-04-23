from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Component(models.Model):

    name = models.CharField(max_length=50)
    usage = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    article_code = models.CharField(max_length=50) 
    quantity = models.CharField(max_length=3)
    supplier = models.CharField(max_length=50)
    img = models.ImageField(null=True, blank=True, upload_to="media/", max_length=255) 
    cost = models.CharField(max_length=50)
    material_compostition = models.CharField(max_length=200)
    component_type = models.CharField(max_length=200, default='EX: BUTTON', editable=True) 

    def __str__(self):
        return self.name



class Bom(models.Model):
    
    style_name= models.CharField(max_length=200)
    style_number= models.CharField(max_length=5)
    created_by = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    season = models.CharField(max_length=4, default='FA20', editable=True)#MAIN SQL QUERY
    category = models.CharField(max_length=25, default='OUTERWEAR', editable=True)
    colorway = models.CharField(max_length=25)
    img = models.ImageField(null=True, blank=True, upload_to="media/", max_length=255)
    component = models.ManyToManyField(Component)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.style_name
    class Meta:
        ordering = ['style_number']


