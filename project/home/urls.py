from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('quiz', views.quiz, name='quiz'),
    path('results', views.results, name='results'),
    path('info', views.info, name='info'),
]