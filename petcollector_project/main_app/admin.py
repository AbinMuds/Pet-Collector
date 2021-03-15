from django.contrib import admin
from .models import Pet, Feeding, Toy, Photo
# Register your models here.

admin.site.register(Pet)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)