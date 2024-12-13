from django.shortcuts import render
from django.http import HttpResponse 
def courses(request):
    return HttpResponse("this is first_app courses page")
def about(request):
    return HttpResponse("this is first_app about page")

def home(request):
    return HttpResponse("this is first_app page")
