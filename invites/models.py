from django.db import models

# Define choices for groups and categories
# Customize these group names as needed
GROUP_CHOICES = [
    ('Family A', 'Falzon Group (Entrée)'),
    ('Team Awesome', 'Lewis Group (Entrée)'),
    ('The Foodies', 'Menor Group (Sides)'),
    ('Neighbors', 'Kent Group (Sides)'),
    ('Sweet Tooth Crew', 'Wilson Group (Desserts)'),
    ('Drink Masters', 'Niro Group (Drinks/Utensils)'),
]

CATEGORY_CHOICES = [
    ('Entrée', 'Entrée'),
    ('Sides', 'Sides'),
    ('Desserts', 'Desserts'),
    ('Drinks/Utensils', 'Drinks/Utensils'),
]

# Create your models here.
class PotluckItem(models.Model):
    """Represents an item being brought to the potluck."""
    submitter_name = models.CharField(
        max_length=100,
        verbose_name="Your Name"
    )
    # Phone number is optional
    submitter_phone = models.CharField(
        max_length=20, # Allow for different formats
        blank=True,
        null=True, # Store NULL in DB if blank
        verbose_name="Your Phone Number (Optional)"
        # Consider adding validation later if needed
    )
    group_name = models.CharField(
        max_length=50, # Increased max_length for longer names
        choices=GROUP_CHOICES,
        verbose_name="Your Assigned Group"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )
    item_description = models.TextField(
        verbose_name="What are you bringing?"
    )
    submitted_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    def __str__(self):
        """String representation of the model."""
        return f"{self.get_category_display()}: {self.item_description} (Brought by: {self.submitter_name} from {self.group_name})"

    class Meta:
        ordering = ['category', 'submitted_at']
        verbose_name = "Potluck Item"
        verbose_name_plural = "Potluck Items"
