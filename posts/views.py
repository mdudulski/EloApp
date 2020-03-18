from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import *
from .forms import *

# Create your views here.

def index(request):
    posts = Post.objects.all()
    players = Player.objects.all()


    form = PlayerForm()


    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('/')



    context = {'posts':posts,
               'players':players,
               'form': form,
               }

    return render(request, 'posts/list.html', context)