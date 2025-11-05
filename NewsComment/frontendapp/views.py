from django.shortcuts import render

def index_view(request):
    return render(request, 'frontend_app/index.html')

def detail_view(request):
    return render(request, 'frontend_app/detail.html')