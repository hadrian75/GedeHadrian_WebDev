
from django.db import migrations
import random
from faker import Faker

def generate_dummy_data(apps, schema_editor):
    """
    Buat data palsu untuk 10 Buku Tabungan, 
    masing-masing dengan JenisTabungan dan beberapa Transaksi.
    """
    
    faker = Faker('id_ID')
    
    JenisTabungan = apps.get_model('tabungan', 'JenisTabungan')
    Buku = apps.get_model('tabungan', 'Buku')
    Transaksi = apps.get_model('tabungan', 'Transaksi')

    JenisTabungan.objects.all().delete() 
    
    jenis_list = []
    jenis_data = [
        {'nama': 'Tabungan Silver', 'bunga_persen': 0.5, 'biaya_admin': 5000},
        {'nama': 'Tabungan Gold', 'bunga_persen': 1.0, 'biaya_admin': 10000},
        {'nama': 'Tabungan Platinum', 'bunga_persen': 1.5, 'biaya_admin': 20000},
    ]
    for data in jenis_data:
        jenis, _ = JenisTabungan.objects.get_or_create(nama=data['nama'], defaults=data)
        jenis_list.append(jenis)

    
    Buku.objects.all().delete() 
    
    buku_list = []
    for _ in range(10):
        buku = Buku.objects.create(
            kantor_bank=faker.company() + " Cabang " + faker.city(),
            nomor_rekening=faker.bban(), 
            nama=faker.name(),
            alamat=faker.address(),
            jenis=random.choice(jenis_list) 
        )
        buku_list.append(buku)

    
    Transaksi.objects.all().delete()
    
    status_choices = ['debit', 'kredit']
    
    for buku in buku_list:
        Transaksi.objects.create(
            buku=buku,
            tanggal=faker.date_between(start_date='-1y', end_date='-11m'), # 1 tahun lalu
            nominal=faker.random_int(min=500000, max=10000000),
            status='kredit'
        )
        
        # Buat 5-15 transaksi acak (debit/kredit)
        for _ in range(random.randint(5, 15)):
            Transaksi.objects.create(
                buku=buku,
                tanggal=faker.date_between(start_date='-10m', end_date='today'), # 10 bulan terakhir
                nominal=faker.random_int(min=50000, max=2000000),
                status=random.choice(status_choices)
            )

class Migration(migrations.Migration):

    dependencies = [
        ('tabungan', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(generate_dummy_data, migrations.RunPython.noop),
    ]