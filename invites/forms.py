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
        # Add Bootstrap classes to each field for modern styling
        self.fields['submitter_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['submitter_phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['group_name'].widget.attrs.update({'class': 'form-select'})
        self.fields['item_description'].widget.attrs.update({'class': 'form-control'})