import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=255, default='images/default.avif') # Gambar produk
    category = models.CharField(max_length=100) # Kain batik, ulos, tenun
    place_of_origin = models.CharField(max_length=100) # daerah asal
    stock = models.IntegerField() # Jumlah stok barang
    availability = models.CharField(max_length=50, default='In Stock') # Ketersediaan

    def __str__(self):
        return self.name # Mengembalikan nama produk sebagai representasi string

