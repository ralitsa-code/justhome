# JustHome

JustHome is a Django web application for a real estate agency. It provides a user interface for browsing property listings and managing real estate information.

## Features

- **Property listings** – browse available properties.
- **Property search** – search for properties by city.
- **Property details** – view information about an individual property.
- **Property management** – create, view, update, and delete property listings.
- **Broker management** – manage real estate broker information.
- **Feature management** – manage property features.
- **Reusable templates** – shared layout components for consistent navigation and page structure.
- **Form validation** – validate user input and display feedback.
- **Custom error page** – display a custom 404 page when a requested page is not found.

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

The project is organized into separate Django applications:

- `real_estate` – property listings and related functionality.
- `broker` – broker information and management.
- `features` – property features.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ralitsa-code/justhome.git
cd justhome
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## Database

The project uses SQLite for local development. Django migrations create the database tables required by the application.

## Purpose

JustHome was developed as a learning project to practise Django fundamentals, including models, forms, views, URL routing, templates, database relationships, validation, and CRUD operations.
