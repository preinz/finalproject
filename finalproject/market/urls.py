from django.contrib import admin
from django.urls import  path

from . import views

urlpatterns = [
    path('', views.presentation, name='presentation'),

    path('login/', views.login,  name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('home/messages.html', views.messages, name='messages'),
    path('home/messages.html/send.html', views.send, name='send'),
    path('home/maths.html', views.maths, name='mathematiques'),
    path('home/exo.html', views.exo, name='exo'),
    path('home/bac.html', views.bac, name='bac-maths'),
    path('home/logout', views.login, name='logout'),
    path('home/covid.html', views.covid, name='covid'),
    path('home/discussion.html', views.chat, name='discussion'),
    path('home/science.html', views.science, name='sciences'),
    path('home/philosophie.html', views.philosophie, name='philosophies'),
    path('home/informatique.html', views.informatique, name='informatiques'),
    path('home/maths.html/complexe.html', views.complexe, name='complexe'),
    path('home/maths.html/fonctions.html', views.fonctions, name='fonctions'),
    path('home/maths.html/primitives.html', views.primitives, name='primitives'),
    path('home/maths.html/integrale.html', views.integrale, name='integrales'),

]