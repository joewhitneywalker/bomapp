from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Bom




# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class BomList(TemplateView):
    template_name ="bom_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["boms"] = Bom.objects.all()
        return context
