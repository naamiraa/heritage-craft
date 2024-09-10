from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_app' : 'HERITAGE CRAFT',
        'npm' : '2306165931',
        'name': 'Namira Aulia',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)