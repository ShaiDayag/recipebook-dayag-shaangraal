from .models import Recipe, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class recipe_list(ListView):
    model = Recipe
    template_name = 'list.html'
    
class recipe(DetailView):
    model = RecipeIngredient
    template_name = 'recipe.html'