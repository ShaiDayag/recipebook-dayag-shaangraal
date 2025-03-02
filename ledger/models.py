from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    name = models.CharField(max_length=100)

class RecipeIngredient(models.Model):
    quantity = models.DecimalField(max_digits=10)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ingredients"
    )

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('ledger:recipe', args=[str(self.pk)])