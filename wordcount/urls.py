
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('count/',views.count,name='count'),
    path('Info/',views.Info,name="Info"),
]
