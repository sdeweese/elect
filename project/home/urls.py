from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('quiz', views.quiz, name='quiz'),
    path('candidates', views.candidates, name='candidates'),
    path('vote', views.vote, name='vote'),
    path('results', views.results, name='results'),

]