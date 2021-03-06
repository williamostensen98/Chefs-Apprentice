from django.contrib import admin
from .models import Recipe, Ingredient, ChosenIngredient, timezone

# Register your models here.)
admin.site.register(Ingredient)
admin.site.site_header = "Chef's Apprentice Admin"
admin.site.site_title = "Chef's Apprentice Admin Portal"
admin.site.index_title = "Welcome to Chef's Apprentice Admin Portal"


class ChosenIngredientInLine(admin.TabularInline):
    model = ChosenIngredient

# definerer hva som skal vises på Recipe displayet i admin siden
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "visible", "author")
    actions = ["make_visible", "make_hidden", "delete_selected"]
    exclude = ('date_posted', 'ingredients')
    inlines = [
        ChosenIngredientInLine,
    ]

    class Meta:
        model = Recipe

    # funksjon for å sette make_visible og hidden som actions i admin siden
    def make_visible(self, request, queryset):
        queryset.update(visible=True)
        queryset.update(date_posted=timezone.now())

    def make_hidden(self, request, queryset):
        queryset.update(visible=False)

# synliggjør disse modellene i admin-siden
admin.site.register(Recipe, RecipeAdmin)
