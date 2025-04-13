from django import forms
from .models import PotluckItem

class PotluckItemForm(forms.ModelForm):
    """Form for users to submit their potluck item."""
    class Meta:
        model = PotluckItem
        # Show all fields needed for user input
        fields = ['submitter_name', 'submitter_phone', 'group_name', 'item_description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Add styling classes or other attributes if needed later
        # self.fields['group_name'].widget.attrs.update({'class': 'form-select'})
        # self.fields['item_description'].widget.attrs.update({'class': 'form-control'}) 