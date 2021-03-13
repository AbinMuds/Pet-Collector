from django.shortcuts import render

# Create your views here.
class Pet:
    def __init__(self, name, species, breed, description, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.description = description
        self.age = age
    
pets = [
    Pet('Lolo', "cat", 'tabby', 'foul little demon', 3),
    Pet('Sachi', "cat", 'tortoise shell', 'diluted tortoise shell', 0),
    Pet('Raven', "cat", 'black tripod', '3 legged cat', 4)
]
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def pets_index(request):
    return render(request, "pets/index.html" , {"pets" : pets})