# admin.py
from django.contrib import admin
from .models import Buku, Transaksi, JenisTabungan # Tambahkan JenisTabungan

# Gunakan @admin.register untuk mendaftarkan Buku dengan BukuAdmin
@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nomor_rekening', 'kantor_bank', 'jenis', 'get_saldo'] # Tambahkan 'jenis'
    search_fields = ['nama', 'nomor_rekening', 'kantor_bank']
    list_filter = ['jenis', 'kantor_bank'] # Tambahkan filter
    
    def get_saldo(self, obj):
        return f"Rp {obj.saldo()}"
    get_saldo.short_description = 'Saldo'

@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'buku', 'status', 'nominal']
    list_filter = ['status', 'tanggal', 'buku']

@admin.register(JenisTabungan)
class JenisTabunganAdmin(admin.ModelAdmin):
    list_display = ['nama', 'bunga_persen', 'biaya_admin']