from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import *

# Create your views here.

def index(request):
    posts = Post.objects.all()
    players = Player.objects.all()

    # Create your views here.
    def run(request):
        player = request.GET['countrySelect']
        print(country)
        return HttpResponse("Completed." + country)




    context = {'posts':posts,
               'players':players,
               }

    return render(request, 'posts/list.html', context)