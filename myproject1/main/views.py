from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>tech with me!</h1>")

def v1(response):
    return HttpResponse("<h1>view 1!</h1>")

def v2(response):
    return HttpResponse("<h1>view 2!</h1> <button> Press </button>")