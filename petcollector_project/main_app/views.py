from django.shortcuts import render
from .models import Pet

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def pets_index(request):
    pets = Pet.objects.all()
    return render(request, "pets/index.html" , {"pets" : pets})