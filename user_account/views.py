from django.shortcuts import render, HttpResponse

from django.http import HttpResponse
from django.template import loader

def useraccount(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())
