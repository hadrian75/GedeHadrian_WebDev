from django.db import models
from django.db.models import Sum


class Buku(models.Model):
    kantor_bank = models.CharField(max_length=100)
    nomor_rekening = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    jenis = models.ForeignKey('JenisTabungan', on_delete=models.CASCADE)

    def saldo(self):
        kredit = self.transaksi_set.filter(status='kredit').aggregate(
            total=Sum('nominal'))['total'] or 0
        debit = self.transaksi_set.filter(status='debit').aggregate(
            total=Sum('nominal'))['total'] or 0
        return kredit - debit
    
    class Meta:
        verbose_name_plural = "Buku Tabungan"
    
    def __str__(self):
        return f"{self.nama}"
      
class Transaksi(models.Model):
    STATUS_CHOICES = [
        ('debit', 'Debit'),
        ('kredit', 'Kredit'),
    ]
    
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='transaksi_set')
    tanggal = models.DateField()
    nominal = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.tanggal} - {self.status} - Rp {self.nominal}"
    
    class Meta:
        verbose_name_plural = "Transaksi"
        ordering = ['-tanggal']

class JenisTabungan(models.Model):
    nama = models.CharField(max_length=50, unique=True)
    bunga_persen = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    biaya_admin = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    keterangan = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Jenis Tabungan"
    
    def __str__(self):
        return self.nama