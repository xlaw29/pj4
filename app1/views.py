from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('This is app 1')
def index1(request):
    return HttpResponse('This is child app 1')