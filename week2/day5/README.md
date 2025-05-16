# Restaurant API Project

A simple Django REST API for managing restaurant menu items.

## Project Structure

- `core/` - Django project settings and main URL configuration
- `app/` - Django application with models, views, and serializers

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Configure PostgreSQL database in `core/settings.py`
6. Run migrations: `python manage.py migrate`
7. Start the server: `python manage.py runserver`

## API Endpoints

- `GET /api/resto/` - List all menu items
- `POST /api/resto/` - Create a new menu item
- `GET /api/resto/<id>/` - Retrieve a specific menu item
- `PUT /api/resto/<id>/` - Update a menu item
- `DELETE /api/resto/<id>/` - Delete a menu item

## Models

### MenuItems
- `item_name` (CharField): Name of the menu item
- `item_price` (SmallIntegerField): Price of the menu item