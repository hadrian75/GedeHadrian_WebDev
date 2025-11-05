from django.contrib import admin

from newsapp.models import Berita
from newsapp.models import Komentar
from django.contrib.admin import site
# Register your models here.
site.register(Berita)
site.register(Komentar)