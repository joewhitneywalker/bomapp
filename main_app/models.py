from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Component(models.Model):#FABRIC MODEL

    name = models.CharField(max_length=50, editable=True)
    usage = models.CharField(max_length=200, editable=True)
    color = models.CharField(max_length=200, editable=True)
    article_code = models.CharField(max_length=50, editable=True) 
    quantity = models.CharField(max_length=3, editable=True)
    supplier = models.CharField(max_length=50, editable=True)
    img = models.ImageField(null=True, blank=True, upload_to="components/", max_length=255) 
    cost = models.CharField(max_length=50, editable=True)
    material_compostition = models.CharField(max_length=200, editable=True)
    component_type = models.CharField(max_length=200, default='EX: BUTTON', editable=True) 

    def __str__(self):
        return self.name





QUANTITY_CHOICES = (
    ('1', '1'), 
    ('2', '2'), 
    ('3', '3'),
    ('4', '4'), 
    ('5', '5'), 
    ('6', '6'), 
    ('7', '7'), 
    ('8', '8'), 
    ('9', '9'), 
    ('10', '10'),   
)

class Trim(models.Model):#TRIM MODEL

    name = models.CharField(max_length=50, editable=True)
    color = models.CharField(max_length=200, editable=True)
    article_code = models.CharField(max_length=50, editable=True) 
    supplier = models.CharField(max_length=50, editable=True)
    img = models.ImageField(null=True, blank=True, upload_to="trims/", max_length=255) 
    cost = models.CharField(max_length=50, editable=True)
    material_compostition = models.CharField(max_length=200, editable=True)
    quantity = models.CharField(max_length=10, choices=QUANTITY_CHOICES, editable=True, default='1')
    placement = models.CharField(max_length=200, editable=True)

    def __str__(self):
        return self.name

class Label(models.Model):#LABEL MODEL

    name = models.CharField(max_length=50, editable=True)
    color = models.CharField(max_length=200, editable=True)
    article_code = models.CharField(max_length=50, editable=True) 
    supplier = models.CharField(max_length=50, editable=True)
    img = models.ImageField(null=True, blank=True, upload_to="labels/", max_length=255) 
    cost = models.CharField(max_length=50, editable=True)
    material_compostition = models.CharField(max_length=200, editable=True)
    quantity = models.CharField(max_length=200, editable=True)
    placement = models.CharField(max_length=200, editable=True)

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
    trim = models.ManyToManyField(Trim)
    label = models.ManyToManyField(Label)
    sketch = models.ImageField(null=True, blank=True, upload_to="sketch/", max_length=255)
    graphic = models.ImageField(null=True, blank=True, upload_to="graphic/", max_length=255)

    def __str__(self):
        return self.style_name
    class Meta:
        ordering = ['style_number']


