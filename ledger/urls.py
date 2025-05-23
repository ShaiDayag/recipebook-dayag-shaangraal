from django.urls import path

from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView

app_name = 'ledger'
urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/add_image/', RecipeUpdateView.as_view(), name='recipe-update'),
]
