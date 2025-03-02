from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, RecipeIngredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'list'
    
class RecipeView(DetailView):
    model = RecipeIngredient
    template_name = 'recipe'