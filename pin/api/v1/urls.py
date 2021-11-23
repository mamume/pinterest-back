
from django.http.response import HttpResponse
from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [

    #path('', hello_world),
    #Create
    path('create', views.pin_create),

    #Read
    ## List all Pins 
    path('pins/', views.pin_list),
    ## List a specific pin 
    path('<int:pk>/', views.single_pin),

    #Update
    path('update/<int:pk>/', views.update_pin),

    #Delete
    path('delete/<int:pk>/', views.delete_pin),


] 
