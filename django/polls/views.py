from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def name(request):
    return HttpResponse("Nama saya hadrian")
def school(request):
    return HttpResponse("Hello Prasmul")

# def index(request):
#   return render(request, "index.html")