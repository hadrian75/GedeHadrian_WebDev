from rest_framework import viewsets
from .models import Berita, Komentar
from .serializers import BeritaSerializer, KomentarSerializer
import django_filters 

class BeritaFilter(django_filters.FilterSet):
    judul = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Berita
        fields = ['judul']

class KomentarFilter(django_filters.FilterSet):
    nama = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Komentar
        fields = ['nama', 'berita']

class BeritaViewSet(viewsets.ModelViewSet):
    queryset = Berita.objects.all()
    serializer_class = BeritaSerializer
    filterset_class = BeritaFilter      

class KomentarViewSet(viewsets.ModelViewSet):
    queryset = Komentar.objects.all()
    serializer_class = KomentarSerializer
    
    filterset_class = KomentarFilter