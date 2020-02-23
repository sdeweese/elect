from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url


from . import views

urlpatterns = [
    #url(r'home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('candidates/', views.candidates, name='candidates'),
    path('vote/', views.vote, name='vote'),
    path('results/', views.results, name='results'),
    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + staticfiles_urlpatterns()
