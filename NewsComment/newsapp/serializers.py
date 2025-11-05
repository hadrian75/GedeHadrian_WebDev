
from rest_framework import serializers
from .models import Berita, Komentar

class KomentarSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Komentar
        fields = ['id', 'nama', 'tgl', 'isi_komentar', 'berita']

class BeritaSerializer(serializers.ModelSerializer):
    komentar = KomentarSerializer(many=True, read_only=True)

    class Meta:
        model = Berita
        fields = ['id', 'judul', 'tgl', 'isi', 'gambar', 'komentar']