from django.shortcuts import render

def index_view(request):
    return render(request, 'frontend_app/index.html')

def detail_view(request):
    return render(request, 'frontend_app/detail.html')
  
  
from django.urls import path
from . import views

urlpatterns = [
    # path '' (root) akan memanggil index_view
    path('', views.index_view, name='index'),
    
    # path 'detail/' akan memanggil detail_view
    # JS di detail.html akan tetap mengambil ID dari query param (?id=)
    path('detail/', views.detail_view, name='detail'),
]