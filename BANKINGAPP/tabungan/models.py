from django.db import models

# Create your models here.
# BUKU
# Kantor Bank
# Nomor Rekening
# Nama 
# Alamat

class Buku(models.Model):
    kantor_bank = models.CharField(max_length=100)
    nomor_rekening = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return f"{self.nama}"