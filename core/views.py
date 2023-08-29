from django.shortcuts import render
from core.models import leaderboard
# Create your views here.

def table(request):
    fm=leaderboard.objects.all()
    return render(request,'core/leaderboard.html',{'fm':fm})

def index(request):
    return render(request,'core/index.html')

def games(request):
    return render(request,'core/games.html')

def astray(request):
    return render(request,'core/astray.html')

def clumsy(request):
    return render(request,'core/clumsy.html')

def master(request):
    return render(request,'core/master.html')

def master2048(request):
    return render(request,'core/master2048.html')

def hextrix(request):
    return render(request,'core/hextrix.html')

def pacman(request):
    return render(request,'core/pacman.html')

def canvas(request):
    return render(request,'core/canvas.html')

def racing(request):
    return render(request,'core/racing.html')

def straight(request):
    return render(request,'core/v1.straight.html')

def snake(request):
    return render(request,'core/snakegame.html')

def monster(request):
    return render(request,'core/monster.html')

def lastwar(request):
    return render(request,'core/lastwar.html')

def goker(request):
    return render(request,'core/goker.html')


def tabletennis(request):
    return render(request,'core/tabletennis.html')


def mysnake(request):
    return render(request,'core/mysnake.html')

def block(request):
    return render(request,'core/block.html')