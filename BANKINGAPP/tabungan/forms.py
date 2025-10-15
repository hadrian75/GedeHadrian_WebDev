from django import forms
from .models import Buku

class BukuTabunganForm(forms.ModelForm):
  class Meta:
    model = Buku
    fields = "__all__"