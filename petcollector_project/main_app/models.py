from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

# Choices to be added on feeding
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # M:M relationship
    toys = models.ManyToManyField(Toy, blank=True)

    def __str__(self):
        return self.name

    # New method for feed_for_today
    def fed_for_today(self):
        return len( self.feeding_set.filter(date=date.today()) )
        
class Feeding(models.Model):
    date = models.DateField("Feeding Date")
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    
    # Create a Pet id FK
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']


    