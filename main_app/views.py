from dataclasses import fields
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Bom, Component, Trim, Label
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


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
        season = self.request.GET.get("season_search")
        category = self.request.GET.get("category_search")
        if style_number != None:
            context["boms"] = Bom.objects.filter(style_number__icontains=style_number)
            context["header"] = f"Searching for {style_number}"
            context['seasons'] =Bom.objects.values_list('season', flat=True).distinct()
            context['categories'] =Bom.objects.values_list('category', flat=True).distinct()
        else:
            context["boms"] = Bom.objects.all()
            context['seasons'] =Bom.objects.values_list('season', flat=True).distinct()
            context['categories'] =Bom.objects.values_list('category', flat=True).distinct()
            context["header"] = "ALL BOMS"
        if season != None:
            context["boms"] = Bom.objects.filter(season__icontains=season)#filters name 
        if category:
            context["boms"] = Bom.objects.filter(category__icontains=category)#filters name 

        return context

def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/boms')





#BOM CREATE VIEW
class Bom_Create(CreateView):
    model = Bom
    fields = '__all__'
    template_name = "bom_create.html"
    def get_success_url(self):
        return reverse('bom_detail', kwargs={'pk': self.object.pk}) 
        

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        #self.object.save_m2m()
        return HttpResponseRedirect('/boms') #update to be on boms detail page

#BOM DETAIL VIEW - WILL BE A TABLE OF COMPONENTS 
class Bom_Detail(DetailView):
    model =  Bom
    template_name = "bom_detail.html"

#BOM SKETCH DETAIL
class Bom_Sketch_Detail(DetailView):
    model =  Bom
    template_name = "bom_sketch_detail.html"

#BOM GRAPHIC DETAIL
class Bom_Graphic_Detail(DetailView):
    model =  Bom
    template_name = "bom_graphic_detail.html"


#BOM UPDATE VIEW
class Bom_Update(UpdateView):
    model = Bom
    fields = '__all__'
    template_name = "bom_update.html"
    def get_success_url(self):
        return reverse('bom_detail', kwargs={'pk': self.object.pk}) 

#BOM DELETE VIEW
class Bom_Delete(DeleteView):
    model = Bom
    template_name = "bom_delete.html"
    success_url = "/boms"





#COMPONENT LIST VIEW
def components_index(request):
    components = Component.objects.all()
    return render(request, 'components_index.html', {'components': components})
#COMPONENT DETAIL VIEW
def components_show(request, component_id):
    component = Component.objects.get(id=component_id)
    return render(request, 'components_show.html', {'component': component}) 
#COMPONENT CREATE VIEW
class Component_Create(CreateView):
    model = Component
    fields = '__all__'
    template_name = "component_create.html"
    success_url = '/components'
#COMPONENT UPDATE VIEW
class Component_Update(UpdateView):
    model = Component
    fields = '__all__'
    template_name = "component_update.html"
    success_url = '/boms'
#COMPONENT DELETE VIEW
class Component_Delete(DeleteView):
    model = Component
    template_name = "component_delete.html"
    success_url = '/components'



#TRIM LIST VIEW
def trims_index(request):
    trims = Trim.objects.all()
    return render(request, 'trims_index.html', {'trims': trims})
#TRIM DETAIL VIEW
def trims_show(request, trim_id):
    trim = Trim.objects.get(id=trim_id)
    return render(request, 'trims_show.html', {'trim': trim}) 
#TRIM CREATE VIEW
class Trim_Create(CreateView):
    model = Trim
    fields = '__all__'
    template_name = "trim_create.html"
    success_url = '/trims'
#TRIM UPDATE VIEW
class Trim_Update(UpdateView):
    model = Trim
    fields = '__all__'
    template_name = "trim_update.html"
    success_url = '/boms'
#TRIM DELETE VIEW
class Trim_Delete(DeleteView):
    model = Trim
    template_name = "trim_delete.html"
    success_url = '/trims'



#LABEL LIST VIEW
def labels_index(request):
    labels = Label.objects.all()
    return render(request, 'labels_index.html', {'labels': labels})
#LABEL DETAIL VIEW
def labels_show(request, label_id):
    label = Label.objects.get(id=label_id)
    return render(request, 'labels_show.html', {'label': label}) 
#TRIM CREATE VIEW
class Label_Create(CreateView):
    model = Label
    fields = '__all__'
    template_name = "label_create.html"
    success_url = '/labels'
#TRIM UPDATE VIEW
class Label_Update(UpdateView):
    model = Label
    fields = '__all__'
    template_name = "label_update.html"
    success_url = '/boms'
#TRIM DELETE VIEW
class Label_Delete(DeleteView):
    model = Label
    template_name = "label_delete.html"
    success_url = '/labels'




#USER FUNCION
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    boms = Bom.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'boms': boms})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})