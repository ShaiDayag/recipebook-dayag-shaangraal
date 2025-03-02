from django.urls import path
from .views import RecipeListView, RecipeView

urlpatterns = [
    path('recipes/list', RecipeListView, name='list'),
    path('recipe/<int:pk>', RecipeView, name='<str:name>'),
]
app_name = "ledger"