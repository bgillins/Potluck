from django.shortcuts import render, redirect, get_object_or_404
from .models import PotluckItem, CATEGORY_CHOICES # Import model and choices
from .forms import PotluckItemForm # Import the form
from collections import defaultdict

# Step 4: Define Group-to-Category Mapping (Updated with new keys)
GROUP_TO_CATEGORY_MAPPING = {
    'Family A': 'Entrée',
    'Team Awesome': 'Entrée',
    'The Foodies': 'Sides',
    'Neighbors': 'Sides',
    'Sweet Tooth Crew': 'Desserts',
    'Drink Masters': 'Drinks/Utensils',
}

# Create your views here.
def potluck_view(request):
    """Handles displaying the form and list, and processing form submissions."""
    if request.method == 'POST':
        form = PotluckItemForm(request.POST)
        if form.is_valid():
            # Don't save to DB yet, need to add category
            potluck_item = form.save(commit=False)
            # Get the selected group name
            selected_group = form.cleaned_data['group_name']
            # Determine the category based on the group
            potluck_item.category = GROUP_TO_CATEGORY_MAPPING.get(selected_group, 'Unknown') # Default if group not found
            # Now save the complete object to the database
            potluck_item.save()
            # Redirect back to the same page after successful submission (PRG pattern)
            # We'll need to define the URL name 'potluck_list' in urls.py later
            return redirect('potluck_list')
        # If form is invalid, it will fall through to the GET request handling below,
        # which will re-render the page with the invalid form (showing errors)

    else: # GET request
        form = PotluckItemForm() # Create a new, empty form

    # Get all submitted items regardless of request method (for display)
    all_items = PotluckItem.objects.all() # Uses ordering from Meta class

    # Group items by category for easier display in the template
    grouped_items = defaultdict(list)
    for item in all_items:
        grouped_items[item.category].append(item)

    # Prepare context for the template
    # Convert defaultdict to dict for template compatibility if needed, though usually works
    # Sort the grouped items based on the order in CATEGORY_CHOICES for consistent display
    category_order = [choice[0] for choice in CATEGORY_CHOICES]
    sorted_grouped_items = {cat: grouped_items[cat] for cat in category_order if cat in grouped_items}

    context = {
        'form': form,
        'grouped_items': sorted_grouped_items, # Pass the sorted grouped items
        'categories': category_order # Pass the category order for the template
    }

    # Render the template
    return render(request, 'invites/potluck.html', context)

# View for editing an existing item
def edit_item_view(request, pk):
    """Handles displaying and processing the form for editing an item."""
    # Get the specific PotluckItem object or return a 404 error if not found
    item_to_edit = get_object_or_404(PotluckItem, pk=pk)

    if request.method == 'POST':
        # Populate the form with submitted data AND the instance being edited
        form = PotluckItemForm(request.POST, instance=item_to_edit)
        if form.is_valid():
            # Don't save to DB yet, need to recalculate category
            potluck_item = form.save(commit=False)
            # Get the potentially updated group name
            selected_group = form.cleaned_data['group_name']
            # Determine the category based on the potentially updated group
            potluck_item.category = GROUP_TO_CATEGORY_MAPPING.get(selected_group, 'Unknown')
            # Save the updated object
            potluck_item.save()
            # Redirect back to the main list view after successful edit
            return redirect('potluck_list')
        # If form is invalid, it will fall through to render the edit page again
        # with the invalid form (showing errors)

    else: # GET request
        # Populate the form with the data from the item being edited
        form = PotluckItemForm(instance=item_to_edit)

    # Prepare context for the template
    context = {
        'form': form,
        'item_to_edit': item_to_edit # Pass the item for context (e.g., in title)
    }

    # Render a new template for editing (or reuse/modify the main one)
    # For simplicity, let's create a dedicated edit template
    return render(request, 'invites/edit_item.html', context)
