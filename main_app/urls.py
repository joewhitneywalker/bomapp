from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('boms/', views.BomList.as_view(), name="bom_list"),
    path('boms/new/', views.Bom_Create.as_view(), name="bom_create"),
    path('boms/<int:pk>/', views.Bom_Detail.as_view(), name="bom_detail"),

    path('boms/<int:pk>/components/<int:component_id>',  views.components_show, name='components_show'), #NESTED ROUTE TO GET COMPONENT DETAILS FROM BOM DETAIL PAGE

    path('boms/<int:pk>/update', views.Bom_Update.as_view(), name="bom_update"), 
    path('boms/<int:pk>delete', views.Bom_Delete.as_view(), name="bom_delete"),


    path('user/<username>/', views.profile, name="profile"),


    path('components/', views.components_index, name='components_index'),
    path('components/<int:component_id>', views.components_show, name='components_show'),
    path('components/create/', views.Component_Create.as_view(), name='component_create'),
    path('components/<int:pk>/update/', views.Component_Update.as_view(), name='component_update'),
    path('components/<int:pk>/delete/', views.Component_Delete.as_view(), name='component_delete'),


    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),


    
]