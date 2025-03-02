from django.db import models

# Ingredient model with name field
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

# Recipe model with name field
class Recipe(models.Model):
    name = models.CharField(max_length=50)

# RecipeIngredient model with ingredient and recipe fields as foreign keys
class RecipeIngredient(models.Model):
    quantity = models.DecimalField(max_digits=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, related_name="ingredients")

def __str__(self):
    return '{}: due on {} unit(s)'.format(self.name, self.due_date)

def get_absolute_url(self):
    return reverse('task_detail', args=[str(self.name)])

# class Task(models.Model):
#     name = models.CharField(max_length=100)
#     due_date = models.DateTimeField(null=False)
#     taskgroup = models.ForeignKey(TaskGroup, on_delete=models.)