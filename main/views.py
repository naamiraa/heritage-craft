from django.shortcuts import render

# Create your views here.
def show_main(request):
    products = [
        { 
            'name': 'Batik Pekalongan',
            'price': "Rp 250000",
            'description': "Batik tulis asli dari Pekalongan dengan motif Batik Semen",
            'image': 'images/batik_pekalongan.avif',
            'category': 'Batik',
            'place_of_origin': 'Pekalongan, Jawa Tengah',
            'stock': 12,
            'availability': 'In Stock',
        }
    ]

    context = {
        'nama_app' : 'HERITAGE CRAFT',
        'npm' : '2306165931',
        'name': 'Namira Aulia',
        'class': 'PBP C',
        'products': products,
    }

    return render(request, "main.html", context)