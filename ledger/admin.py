from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    fieldsets = [
        ('Details', {
            'fields': [
                ('quantity'), 'ingredient', 'recipe'
            ]
        }),
    ]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
