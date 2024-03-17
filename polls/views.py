from django.shortcuts import render

from django.http import HttpResponse,HttpRequest


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request):
    return HttpResponse("This is the detail page of question")