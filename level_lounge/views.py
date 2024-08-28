from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_forum(request):
    return HttpResponse("What's you favourite game?")
