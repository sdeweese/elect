from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return HttpResponse("Hello, world. This is our homepage.")

def quiz(request):
    return HttpResponse("Quiz page")

def results(request):
    return HttpResponse("Results page")

def info(request):
    return HttpResponse("Info page")
