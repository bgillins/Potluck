from django.contrib import admin
from .models import PotluckItem # Import the model

# Register your models here.
@admin.register(PotluckItem)
class PotluckItemAdmin(admin.ModelAdmin):
    """Admin configuration for PotluckItem model."""
    list_display = ('item_description', 'submitter_name', 'group_name', 'category', 'submitted_at')
    list_filter = ('category', 'group_name')
    search_fields = ('item_description', 'submitter_name')
    # Make submitted_at read-only as it's set automatically
    readonly_fields = ('submitted_at',)
    # You can customize the fields displayed in the edit form:
    # fields = ('submitter_name', 'submitter_phone', 'group_name', 'item_description') # Excludes category & submitted_at

# Alternative basic registration:
# admin.site.register(PotluckItem)
