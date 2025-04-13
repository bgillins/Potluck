from django.urls import path
from . import views

# app_name = 'invites' # Optional: Add namespace if you have many apps

urlpatterns = [
    # Map the root URL of this app ('') to the potluck_view (list and add)
    path('', views.potluck_view, name='potluck_list'),
    # URL for editing an item. <int:pk> captures the item ID.
    path('edit/<int:pk>/', views.edit_item_view, name='edit_item'),
] 