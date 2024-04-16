from django.shortcuts import render, HttpResponse

from django.http import HttpResponse
from django.template import loader

def useraccount(request):
    return render(request, "test.html")
