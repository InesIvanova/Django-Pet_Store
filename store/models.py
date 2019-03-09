from django.db import models
from Scripts.PetStore.store import variables
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
import os.path,sys

CURRENT_DIR = os.path.dirname(__file__).replace('\\','/')
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
IMAGES_PATH = f'{CURRENT_DIR}/static/images'


class Animal(models.Model):
    KIND_ANIMAL_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('unknown', 'No information')
    ]
    DOG_BREEDS = variables.dog_breeds
    CAT_BREEDS = variables.cats_breed
    BREEDS = variables.all_breeds
    COLORS = variables.basic_colors

    name = models.CharField(max_length=20, blank=True, default=None)
    age = models.PositiveIntegerField(blank=True, default='unknown')
    kind = models.CharField(max_length=20, choices=KIND_ANIMAL_CHOICES, blank=True, default='unknown')
    breed = models.CharField(max_length=20, choices=BREEDS, blank=True, default='unknown')
    color = models.CharField(max_length=20, choices=COLORS)
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to = 'animals', default='animals/default.jpg', max_length=500)

    def __str__(self):
        return f'{self.name} {self.age} {self.kind} {self.breed} {self.color} {self.price} {self.image}'

    def get_breed(self):
        for breed in self.BREEDS:
            if breed[0] == self.breed:
                return breed[1]

    def get_color(self):
        for color in self.COLORS:
            if color[0] == self.color:
                return color[1]


class Question(models.Model):
    email = models.EmailField()
    question = models.CharField(max_length=400)

    def __str__(self):
        return f'from {self.email} question: {self.question}'

