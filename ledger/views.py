from .models import Recipe, RecipeIngredient
from .views import ListView, DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/templates/list.html'
    
class RecipeView(DetailView):
    model = RecipeIngredient
    template_name = 'ledger/templates/recipe.html'