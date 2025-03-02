from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def recipe_list(request):
    recipes = Recipe.objects.all()
    recipe_list = {
        "recipes": recipes
    }
    return render(request, "list.html", recipe_list)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html' # this is the default value
    
class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html' #this is the default value

def recipe_1(request):
    recipe_1 = {
        "name": "Recipe 1",
        "ingredients": [
            {
                "name": "tomato",
                "quantity": "3pcs"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "pork",
                "quantity": "1kg"
            },
            {
                "name": "water",
                "quantity": "1L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
        "link": "/recipe/1"
    }
    return render(request, "1.html", recipe_1)

def recipe_2(request):
    recipe_2 = {
        "name": "Recipe 2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
        "link": "/recipe/2"
    }
    return render(request, "2.html", recipe_2)
