from rest_framework import serializers
from .models import Buku, Transaksi, JenisTabungan

class JenisTabunganSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenisTabungan
        fields = ['id', 'nama', 'bunga_persen', 'biaya_admin', 'keterangan']

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = "__all__"

class BukuSerializer(serializers.ModelSerializer):
    saldo = serializers.SerializerMethodField()
    transaksi_set = TransaksiSerializer(many=True, read_only=True)
    
    class Meta:
        model = Buku
        fields = "__all__"
        
    def get_saldo(self, obj):
        return obj.saldo()

class BukuListSerializer(serializers.ModelSerializer):
    saldo = serializers.SerializerMethodField()
    
    class Meta:
        model = Buku
        fields = "__all__"
        
    def get_saldo(self, obj):
        return obj.saldo()