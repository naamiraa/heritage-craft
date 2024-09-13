from django.urls import path
from main import views
from main.views import show_main, create_product_entry

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', views.show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
]