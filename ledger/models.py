from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.pk)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50, default='NULL')
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.pk)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.SET_NULL,
        null=True,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        related_name='ingredients'
    )

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        related_name='image'
    )
