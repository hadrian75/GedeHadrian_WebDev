from django import forms
from .models import Buku, Transaksi

class BukuTabunganForm(forms.ModelForm):
  class Meta:
    model = Buku
    fields = "__all__"
    

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = [ 'status', 'nominal']
    