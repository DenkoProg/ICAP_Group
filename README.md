# Django Product Management API

An API service built with Django and Django REST Framework to manage products. Ensures authentication and authorization, allowing only superusers to access the product management functionalities.

## Features

- **CRUD Operations:** Manage products (Create, Retrieve, Update, Delete)
- **Superuser Restriction:** Only superusers can perform CRUD operations
- **Filters:** Retrieve products based on certain parameters (e.g., offer of the month, availability, self-pickup)

## Prerequisites

Ensure you have the following installed:
- Python (3.6 or higher)
- pip (Python’s package installer)
- virtualenv (optional, for creating isolated Python environments)

## Installation

1. **Clone Repository:**
   ```bash
   git clone https://github.com/your_username/your_repo_name.git

### Navigate to Project Directory:
    ```bash
    cd path_to_your_project

### Setup Virtual Environment (Optional, but Recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate  # For Windows

### Install Dependencies
    ```bash
    pip install -r requirements.txt

### Migrate Database
    ```bash
    python manage.py migrate

### Create Superuser:
     ```bash
    python manage.py createsuperuser

Follow the prompts to create a superuser account.

### Run Development Server:
    ```bash
    python manage.py runserver

2. **Usage**

## Login
    Navigate to http://127.0.0.1:8000/login/ and login with superuser credentials.

## API Endpoints:
# Retrieve & Create Products: http://127.0.0.1:8000/products/
# Retrieve, Update & Delete a Single Product: http://127.0.0.1:8000/products/{product_id}/

## Filters
# Apply filters by appending query parameters to the URL: