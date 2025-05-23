from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    fieldsets = [
        ('Details', {
            'fields': [
                ('quantity'), 'ingredient', 'recipe'
            ]
        })
    ]


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    fieldsets = [
        ('Details', {
            'fields': [
                ('image', 'description'), 'recipe'
            ]
        })
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
