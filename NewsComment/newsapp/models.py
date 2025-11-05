from django.db import models

class Berita(models.Model):
    judul = models.CharField(max_length=255)
    tgl = models.DateTimeField(auto_now_add=True) 
    isi = models.TextField()
    gambar = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.judul

class Komentar(models.Model):
    nama = models.CharField(max_length=100)
    tgl = models.DateTimeField(auto_now_add=True)
    isi_komentar = models.TextField()
    berita = models.ForeignKey(
        Berita, 
        on_delete=models.CASCADE, 
        related_name='komentar'  
    )

    def __str__(self):
        return f"Komentar oleh {self.nama} di {self.berita.judul}"