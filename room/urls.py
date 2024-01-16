
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "rooms"
urlpatterns = [
    path("",views.rooms,name ="rooms"),
    path("detail/<int:id>/",views.detail,name ="detail")


]
