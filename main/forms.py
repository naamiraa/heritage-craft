from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "image", "category", "place_of_origin", "stock", "availability"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_image(self):
        image = self.cleaned_data["image"]
        return strip_tags(image)

    def clean_category(self):
        categpry = self.cleaned_data["category"]
        return strip_tags(categpry)
    
    def clean_place_of_origin(self):
        place_of_origin = self.cleaned_data["place_of_origin"]
        return strip_tags(place_of_origin)
    
    def clean_availability(self):
        availability = self.cleaned_data["availability"]
        return strip_tags(availability)
