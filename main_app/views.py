from dataclasses import fields
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Bom, Component
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/boms') #update to be on boms detail page

#BOM DETAIL VIEW - WILL BE A TABLE OF COMPONENTS 
class Bom_Detail(DetailView):
    model =  Bom
    template_name = "bom_detail.html"

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
    success_url = "/boms/"


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










def components_index(request):
    components = Component.objects.all()
    return render(request, 'component_index.html', {'components': components})

def components_show(request, component_id):
    component = Component.objects.get(id=component_id)
    return render(request, 'component_show.html', {'component': component}) 

class Component_Create(CreateView):
    model = Component
    fields = '__all__'
    template_name = "component_create.html"
    success_url = '/components'

class Component_Update(UpdateView):
    model = Component
    fields = '__all__'
    template_name = "component_update.html"
    success_url = '/components'

class Component_Delete(DeleteView):
    model = Component
    template_name = "component_delete.html"
    success_url = '/components'
