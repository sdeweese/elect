from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from home.forms import survey 
from home.models import surveyModel


def showform(request):
    form = survey(request.POST)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return HttpResponseRedirect('/home')


# Create your views here.
def home(request):
    #return HttpResponse("Hello, world. This is our homepage.")
    return render(request, "index.html")

def quiz(request):
    #return HttpResponse("Quiz page")
    if(request.method == 'POST'):
        form = survey(request.POST)
        if(form.is_valid()):
            form.save()
        context = {'form': form }   
        return render(request, 'result', context) 
    return render(request, "quiz.html")

def candidates(request):
    #return HttpResponse("Results page")
    return render(request, "candidates.html")

def vote(request):
    #return HttpResponse("Info page")
    return render(request, "vote.html")

def results(request):
    return render(request, "results.html")
