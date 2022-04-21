from dataclasses import fields
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Bom
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse



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
    def get_success_url(self):
        return reverse('bom_detail', kwargs={'pk': self.object.pk}) 

#BOM DETAIL VIEW - WILL BE A TABLE OF COMPONENTS 
class Bom_Detail(DetailView):
    model =  Bom
    template_name = "bom_detail.html"


class Bom_Update(UpdateView):
    model = Bom
    fields = '__all__'
    template_name = "bom_update.html"
    def get_success_url(self):
        return reverse('bom_detail', kwargs={'pk': self.object.pk}) 

class Bom_Delete(DeleteView):
    model = Bom
    template_name = "bom_delete.html"
    success_url = "/boms/"
