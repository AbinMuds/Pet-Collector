from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Pet, Toy
from .forms import FeedingForm, PetForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

# Views for page with all pets
@login_required
def pets_index(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, "pets/index.html", {"pets" : pets})

# To create new pets 
@login_required
def pets_new(request):
    # create a instance of the petform filled with submitted values or nothing
    pet_form = PetForm(request.POST or None)
    if request.POST and pet_form.is_valid:
        new_cat = pet_form.save(commit=False)
        new_cat.user = request.user
        new_cat.save()
        return redirect('index')
    else:
        return render(request, "pets/new.html", {"pet_form" : pet_form})

# edit pet details
@login_required
def pets_edit(request, pet_id):
    # instance of Pet
    pet = Pet.objects.get(id=pet_id)
    pet_form = PetForm(request.POST or None, instance=pet)
    if request.POST and pet_form.is_valid:
        pet_form.save()
        return redirect('detail', pet_id=pet_id)
    else:
        return render(request, 'pets/edit.html', { 'pet': pet, 'pet_form': pet_form })

# Delete pets
@login_required
def pets_delete(request, pet_id):
    Pet.objects.get(id=pet_id).delete()
    return redirect('index')

# Views for page with the detail of the pet with its id
@login_required
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

@login_required
def add_feeding(request, pet_id):
    # create a ModelForm using data in request.POST
    form = FeedingForm(request.POST)
    # validate the form 
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pet_id = pet_id
        new_feeding.save()
    return redirect('detail', pet_id=pet_id)
    
@login_required
def assoc_toy(request, pet_id, toy_id):
    Pet.objects.get(id=pet_id).toys.add(toy_id)
    return redirect('detail', pet_id=pet_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            print(form.errors.as_json())
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)




