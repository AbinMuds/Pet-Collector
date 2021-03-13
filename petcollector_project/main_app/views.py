from django.shortcuts import render
from .models import Pet

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

# Views for page with all pets
def pets_index(request):
    pets = Pet.objects.all()
    return render(request, "pets/index.html" , {"pets" : pets})

# Views for page with the detail of the pet with its id
def pets_detail(request, pet_id):
    pet = Pet.objects.get(id = pet_id)
    return render(request, "pets/detail.html", {"pet" : pet})

