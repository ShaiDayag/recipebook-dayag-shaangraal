from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeImageForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeForm()
        context['recipes'] = Recipe.objects.all()
        return context


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeImageForm()
        context['recipe'] = self.get_object()
        context['images'] = RecipeImage.objects.filter(recipe=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = self.request.user.username
            form.instance.recipe = self.get_object()
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/recipe_form.html'
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.author = self.request.user.username
        form.save()
        return super(RecipeCreateView, self).form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'ledger/recipe_image_form.html'
    form_class = RecipeImageForm