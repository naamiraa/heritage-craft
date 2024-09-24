import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.TextField(default='https://private-user-images.githubusercontent.com/178132521/369594940-09a367c0-0869-411b-ba75-36b21d9e21b5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjcxODk2MDMsIm5iZiI6MTcyNzE4OTMwMywicGF0aCI6Ii8xNzgxMzI1MjEvMzY5NTk0OTQwLTA5YTM2N2MwLTA4NjktNDExYi1iYTc1LTM2YjIxZDllMjFiNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkyNFQxNDQ4MjNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02ZTExMTdmYTVkMDEzZGY0M2E4NWUyM2EwZGFiOTBmODJiMzE1Y2M1NzdmZTQ4NjQ4ODJmZDk3YjFkNjdjMWVjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.EAR_fR-_8DooRA-p0PTyiAzKRKQFQmTsxukcNmxVJg4') # Gambar produk
    category = models.CharField(max_length=100) # Kain batik, ulos, tenun
    place_of_origin = models.CharField(max_length=100) # daerah asal
    stock = models.IntegerField() # Jumlah stok barang
    availability = models.CharField(max_length=50, default='In Stock') # Ketersediaan

    def __str__(self):
        return self.name # Mengembalikan nama produk sebagai representasi string

