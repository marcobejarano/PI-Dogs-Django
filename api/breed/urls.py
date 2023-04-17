from .views.get_dogs import get_dogs
from django.urls import path

urlpatterns = [
    path('dogs/', get_dogs, name='get_dogs'),
]