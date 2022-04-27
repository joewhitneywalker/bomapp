from django.contrib import admin
from .models import Bom, Component, Trim, Label

# Register your models here.
admin.site.register(Bom)
admin.site.register(Component)
admin.site.register(Trim)
admin.site.register(Label)