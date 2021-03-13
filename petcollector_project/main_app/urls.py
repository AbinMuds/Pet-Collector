from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('pets/', views.pets_index, name="index"),
    path('pets/<int:pet_id>/', views.pets_detail, name="detail"),
    path('pets/<int:pet_id>/add_feeding/', views.add_feeding, name="add_feeding"),
    # associate a toy with a pet
    path('pets/<int:pet_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # create a new pet
    path('pets/new/', views.pets_new, name="new"),
    path('pets/<int:pet_id>/edit/', views.pets_edit, name="edit"),
    path('pets/<int:pet_id>/delete/', views.pets_delete, name="delete"),
]