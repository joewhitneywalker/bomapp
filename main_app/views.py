from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView




# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class Bom:
    def __init__(self, style_number, description, created_at, created_by, season, category, colorways,):
        self.style_number = style_number
        self.description = description
        self.created_at = created_at
        self.created_by = created_by
        self.season = season
        self.category = category
        self.colorways = colorways

boms = [
    Bom("A0001", "PULL ON SHORT-COTTON NYLON RIPSTOP", "4/1722", "JOE WALKER", "SPRING", "BOTTOMS", "RED, BLUE, KHAKI" ),
    Bom("A0002", "PULL ON SHORT-COTTON CANVAS", "4/1722", "JOE WALKER", "SPRING", "BOTTOMS", "WHITE, BLACK, OLIVE" )
]

class BomList(TemplateView):
    template_name ="bom_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["boms"] = boms 
        return context