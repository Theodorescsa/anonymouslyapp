from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import RoomModel
# Create your views here.
def rooms(request):
    rooms = RoomModel.objects.all()
    context = {
        'rooms':rooms
    }
    return render(request,"room/room.html",context)

def detail(request,id):
    room = RoomModel.objects.get(id=id)
    context = {
        'room':room
    }
    return render(request,"room/detail.html",context)