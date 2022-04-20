from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Bom




# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["boms"] = Bom.objects.all()
        return context





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



