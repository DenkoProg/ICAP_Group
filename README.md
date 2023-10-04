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
   git clone https://github.com/DenkoProg/ICAP_Group.git

### Setup Virtual Environment (Optional, but Recommended):
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate  # For Windows

### Install Dependencies
    pip install -r requirements.txt

### Migrate Database
    python manage.py migrate

### Create Superuser:
    python manage.py createsuperuser

Follow the prompts to create a superuser account.

### Run Development Server:
    python manage.py runserver

2. **Usage**

## Login
    Navigate to http://127.0.0.1:8000/login/ and login with superuser credentials.

## API Endpoints:
### Retrieve & Create Products: http://127.0.0.1:8000/products/
### Retrieve, Update & Delete a Single Product: http://127.0.0.1:8000/products/{product_id}/

## Filters
### Apply filters by appending query parameters to the URL:
    http://127.0.0.1:8000/products/?offer_of_the_month=true&availability=true
