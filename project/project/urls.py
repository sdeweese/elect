from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('quiz', views.quiz, name='quiz'),
    path('candidates', views.candidates, name='candidates'),
    path('vote', views.vote, name='vote'),
    path('results', views.results, name='results'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + staticfiles_urlpatterns()
