from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    # Kain batik, ulos, tenun, & berbagai kerajinan tangan
    category = models.CharField(max_length=100)
    # daerah asal
    place_of_origin = models.CharField(max_length=100)
    # tanggal penambahan produk
    date = models.DateField(auto_now_add=True)

