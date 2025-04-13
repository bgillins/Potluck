# Potluck Coordination App - Development Plan

This document outlines the steps to build the Potluck coordination web application using Python and Django.

**Goal:** Create a simple web page with a form where users can select their assigned group, describe the item they are bringing for a potluck, and view a categorized list of all submitted items.

**Technology Stack:**
*   **Backend:** Python 3.x, Django
*   **Database:** SQLite (default with Django, suitable for simple projects and free hosting tiers)
*   **Frontend:** Basic HTML, CSS (Rendered by Django Templates)
*   **Hosting:** PythonAnywhere / Render (or similar free/hobby tier platform)

---

## Development Steps:

### 1. Project Setup

*   **Install Python:** Ensure Python 3.8+ is installed.
*   **Create Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
*   **Install Django:**
    ```bash
    pip install django
    ```
*   **Create Django Project:**
    ```bash
    django-admin startproject potluck_project . # Note the '.' to create in current dir
    ```
*   **Create Django App:** This app will handle the potluck logic.
    ```bash
    python manage.py startapp invites
    ```
*   **Register App:** Add `'invites'` to the `INSTALLED_APPS` list in `potluck_project/settings.py`.
*   **Initial Migration:** Run initial database migrations.
    ```bash
    python manage.py migrate
    ```
*   **Run Development Server:** Check if the setup works.
    ```bash
    python manage.py runserver
    ```
    (Access `http://127.0.0.1:8000/` in your browser)

### 2. Define Data Model (`invites/models.py`)

*   Define a model `PotluckItem` to store submissions.
*   Fields needed:
    *   `group_name`: To store which group the person belongs to (e.g., "Group 1", "Group 2", ... "Group 6"). Use `CharField` with choices.
    *   `category`: The food category (e.g., "Entrée", "Sides", "Desserts", "Drinks/Utensils"). Use `CharField` with choices. This will be determined based on the `group_name`.
    *   `item_description`: What the person is bringing. Use `TextField`.
    *   `submitted_at`: Timestamp of submission. Use `DateTimeField` with `auto_now_add=True`.

### 3. Create Database Migrations

*   After defining the model in `invites/models.py`:
    ```bash
    python manage.py makemigrations invites
    python manage.py migrate
    ```

### 4. Define Group-to-Category Mapping

*   Establish the mapping in `invites/views.py` or a separate configuration file/dictionary.
    *   Example Mapping:
        *   Group 1, Group 2: Entrée
        *   Group 3, Group 4: Sides
        *   Group 5: Desserts
        *   Group 6: Drinks/Utensils

### 5. Create the Form (`invites/forms.py`)

*   Create a new file `invites/forms.py`.
*   Define a Django `ModelForm` based on the `PotluckItem` model.
*   The form should only display fields for `group_name` (as a dropdown) and `item_description`. The `category` will be set programmatically in the view.

### 6. Create the View (`invites/views.py`)

*   Create a view function (e.g., `potluck_view`).
*   **GET Request:**
    *   Create an instance of the form.
    *   Query all existing `PotluckItem` objects from the database.
    *   Group the items by `category` for display.
    *   Render the template, passing the form and the grouped items.
*   **POST Request:**
    *   Instantiate the form with submitted data (`request.POST`).
    *   Check if the form is valid (`form.is_valid()`).
    *   If valid:
        *   Get the selected `group_name`.
        *   Determine the corresponding `category` using the mapping defined in Step 4.
        *   Create a `PotluckItem` instance but don't save it yet (`commit=False`).
        *   Set the `category` on the instance.
        *   Save the complete instance to the database (`form.save()` or `instance.save()`).
        *   Redirect back to the same view/URL to show the updated list and a fresh form (Post/Redirect/Get pattern).
    *   If invalid:
        *   Re-render the template with the form containing error messages and the existing potluck items (similar to GET).

### 7. Create the Template (`invites/templates/invites/potluck.html`)

*   Create the directory structure: `invites/templates/invites/`.
*   Create the `potluck.html` file.
*   Use HTML and Django template tags:
    *   Display the form (`{{ form.as_p }}` or loop through fields manually). Include a CSRF token (`{% csrf_token %}`).
    *   Display the submitted items:
        *   Loop through the categories ("Entrée", "Sides", etc.).
        *   For each category, loop through the items belonging to it and display the `item_description` (and optionally the `group_name`).

### 8. Configure URLs

*   **App URLs (`invites/urls.py`):**
    *   Create this file.
    *   Define a URL pattern (e.g., path `''`) that maps to the `potluck_view`. Give it a name (e.g., `'potluck_list'`).
*   **Project URLs (`potluck_project/urls.py`):**
    *   Include the `invites.urls` into the main project URLs using `include()`. For example, `path('', include('invites.urls'))`.

### 9. Basic Styling (Optional)

*   Add a simple CSS file (`invites/static/invites/style.css`).
*   Configure static files in `potluck_project/settings.py`.
*   Load the static files in `potluck.html` and apply basic styles for readability.

### 10. Admin Interface (Optional Enhancement)

*   Register the `PotluckItem` model in `invites/admin.py` to manage entries via the Django admin site (`/admin/`).
*   Create a superuser: `python manage.py createsuperuser`.

### 11. Deployment

*   Choose a hosting provider (e.g., PythonAnywhere, Render).
*   Follow their specific Django deployment guides.
*   Key steps usually involve:
    *   Setting up `ALLOWED_HOSTS` in `settings.py`.
    *   Configuring static files.
    *   Setting `DEBUG = False`.
    *   Setting up the WSGI configuration.
    *   Pushing code to a Git repository (e.g., GitHub) and connecting it to the hosting provider.

---

This plan provides a roadmap. We can tackle each step sequentially. Let me know when you're ready to start with Step 1 or if you have any questions! 