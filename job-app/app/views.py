from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def job_detail(request, id):
    return HttpResponse("Job detail page!")


    # "<domain>/job/1" -->Job Detail page
