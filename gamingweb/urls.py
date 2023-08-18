"""gamingweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leaderboard/',views.table,name='leaderboard'),
    path('',views.index,name='index'),
    path('games/',views.games,name='games'),
    path('astray/',views.astray,name='astray'),
    path('clumsy/',views.clumsy,name='clumsy'),
    path('master/',views.master,name='master'),
    path('master2048/',views.master2048,name='master2048'),
    path('hextrix/',views.hextrix,name='hextrix'),
    path('pacman/',views.pacman,name='pacman'),
    path('canvas/',views.canvas,name='canvas'),
    path('racing/',views.racing,name='racing'),
    path('racing/v1.straight.html/',views.straight,name='straight'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
