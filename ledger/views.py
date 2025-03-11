from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe, RecipeIngredient


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = RecipeIngredient
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'registration/login.html'
