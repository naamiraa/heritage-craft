from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'nama_app' : 'HERITAGE CRAFT',
        'npm' : '2306165931',
        'name': 'Namira Aulia',
        'class': 'PBP C',
        'product_entries': product_entries,
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product_entry.html", context)

