from django.shortcuts import render, redirect
from .models import Pet
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    context = {
        "pet" : pet,
        "feeding_form" : feeding_form
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



