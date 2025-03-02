from django.urls import path
from .views import RecipeListView, RecipeView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='list.html'),
    path('recipe/<int:pk>', RecipeView.as_view(), name='recipe.html'),
]
app_name = "ledger"