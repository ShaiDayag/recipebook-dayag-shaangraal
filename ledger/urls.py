from django.urls import path
from .views import RecipeListView, RecipeView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>', RecipeView.as_view(), name='<str:name>'),
]
app_name = "ledger"