from django.contrib import admin

from .models import Pantry




@admin.register(Pantry)
class PantryAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'website']
