from django.shortcuts import get_object_or_404, render
from .models import Buku
from .forms import BukuTabunganForm, TransaksiForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from rest_framework import viewsets, status
from django.db.models import Sum
from .models import Buku, Transaksi, JenisTabungan
from .serializers import (
    BukuSerializer, 
    BukuListSerializer, 
    TransaksiSerializer,
    JenisTabunganSerializer
)
# Create your views here.
def list_buku(request):
    list_buku = Buku.objects.all()
    data = {"list_buku": list_buku}
    return render(request, "buku/list.html", data)
  
def create_buku(request):
  form = BukuTabunganForm(request.POST or None)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse("tabungan:list-buku"))
  data = {}
  data["form"] = form
  return render(request, "buku/create.html", data)

def update_buku(request, buku_id):
  obj = get_object_or_404(Buku, id=buku_id)
  form = BukuTabunganForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse("tabungan:list-buku"))
  context = {}
  context["form"] = form
  return render(request, "buku/update.html", context)

def delete_buku(request, buku_id):
  obj = get_object_or_404(Buku, id=buku_id)
  if request.method == "POST":
    obj.delete()
    return HttpResponseRedirect(reverse("tabungan:list-buku"))
  context = {'obj' : obj}
  return render(request, "buku/delete.html", context)

def detail_buku(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    transaksi_list = buku.transaksi_set.all()
    context = {
        'buku': buku,
        'transaksi_list': transaksi_list
    }
    return render(request, "buku/detail.html", context)

def tambah_transaksi(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    if request.method == 'POST':
        form = TransaksiForm(request.POST)
        if form.is_valid():
            transaksi = form.save(commit=False)
            transaksi.buku = buku
            transaksi.tanggal = date.today()
            transaksi.save()
            return redirect('tabungan:detail-buku', buku_id=buku_id)
    else:
        form = TransaksiForm()
    context = {'form': form, 'buku': buku}
    return render(request, 'buku/transaksi.html', context)
  
class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BukuListSerializer
        return BukuSerializer

class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
    http_method_names = ['get', 'post', 'patch', 'head', 'options']
class JenisTabunganViewSet(viewsets.ModelViewSet):
    queryset = JenisTabungan.objects.all()
    serializer_class = JenisTabunganSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']