from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe, RecipeIngredient


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'


class RecipeDetailView(DetailView):
    model = RecipeIngredient
    template_name = 'ledger/recipe.html'
