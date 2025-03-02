from django.urls import path
from .views import RecipeListView, RecipeView

urlpatterns = [
    path('recipes/list', recipe_list, name='list'),
    path('recipe/<int:pk>', recipe, name='<str:name>'),
]
app_name = "ledger"