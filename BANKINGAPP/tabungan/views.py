from django.shortcuts import get_object_or_404, render
from .models import Buku
from .forms import BukuTabunganForm
from django.http import HttpResponseRedirect
from django.urls import reverse
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
  