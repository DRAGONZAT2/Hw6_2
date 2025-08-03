from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner', 'birth_date', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('name', 'owner__email')
