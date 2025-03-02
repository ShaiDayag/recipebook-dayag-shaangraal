from .models import Recipe, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/templates/list.html'
    
class RecipeView(DetailView):
    model = RecipeIngredient
    template_name = 'ledger/templates/recipe.html'