from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

def index(request):
    posts = Post.objects.all()
    players = Player.objects.all()


    context = {'posts':posts,
               'players':players,
               }

    return render(request, 'posts/list.html', context)