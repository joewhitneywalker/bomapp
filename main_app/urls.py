from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('boms/', views.BomList.as_view(), name="bom_list"),
    path('boms/new/', views.Bom_Create.as_view(), name="bom_create"),
]