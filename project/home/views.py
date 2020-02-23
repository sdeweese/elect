from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    #return HttpResponse("Hello, world. This is our homepage.")
    return render(request, "index.html")

def quiz(request):
    #return HttpResponse("Quiz page")
    return render(request, "quiz.html")

def results(request):
    #return HttpResponse("Results page")
    return render(request, "results.html")

def info(request):
    #return HttpResponse("Info page")
    return render(request, "info.html")
