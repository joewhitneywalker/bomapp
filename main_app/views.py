from dataclasses import fields
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Bom
from django.views.generic.edit import CreateView




# Create your views here.

#HOME VIEW WHICH SHOWS USER'S RECENT FILES
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["boms"] = Bom.objects.all()
        return context




#BOM LIST VIEW WITH SEARCH FEATURE
class BomList(TemplateView):
    template_name ="bom_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        style_number = self.request.GET.get("style_number")
        if style_number != None:
            context["boms"] = Bom.objects.filter(style_number__icontains=style_number)
            context["header"] = f"Searching for {style_number}"
        else:
            context["boms"] = Bom.objects.all()
            context["header"] = "ALL BOMS"
        return context


#BOM CREATE VIEW
class Bom_Create(CreateView):
    model = Bom
    fields = '__all__'
    template_name = "bom_create.html"
    success_url = "/boms/"
