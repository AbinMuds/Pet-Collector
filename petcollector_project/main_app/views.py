from django.shortcuts import render, redirect
from .models import Pet, Toy
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

# Views for page with all pets
def pets_index(request):
    pets = Pet.objects.all()
    return render(request, "pets/index.html" , {"pets" : pets})

# To create new pets 
def pets_new(request):
    pass

# Views for page with the detail of the pet with its id
def pets_detail(request, pet_id):
    pet = Pet.objects.get(id = pet_id)
    # Get the toys that pet dosen't have
    toys_pet_doesnt_have = Toy.objects.exclude(id__in = pet.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    context = {
        "pet" : pet,
        "feeding_form" : feeding_form,
        "toys" : toys_pet_doesnt_have
    }
    return render(request, "pets/detail.html", context)

def add_feeding(request, pet_id):
    # create a ModelForm using data in request.POST
    form = FeedingForm(request.POST)
    # validate the form 
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pet_id = pet_id
        new_feeding.save()
    return redirect('detail', pet_id=pet_id)

def assoc_toy(request, pet_id, toy_id):
    Pet.objects.get(id=pet_id).toys.add(toy_id)
    return redirect('detail', pet_id=pet_id)




