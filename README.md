# Restaurant Store

A simple Django-based online store for a restaurant, allowing customers to browse products, view details, and use a basic cart functionality.

## Features

- Product listing with images and details
- Product detail view
- Shopping cart functionality (add/update/remove items)
- Admin panel for product management (add/edit/delete)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd restaurant_store
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   
   If requirements.txt doesn't exist, install Django and Pillow:
   ```
   pip install django pillow
   ```

5. Apply database migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser for the admin panel:
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to set up username, email, and password.

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the site at http://127.0.0.1:8000/ and admin panel at http://127.0.0.1:8000/admin/

## Usage

### Adding Products
1. Log in to the admin panel (http://127.0.0.1:8000/admin/) with your superuser credentials
2. Navigate to Products section and click "Add Product"
3. Fill in the product details (name, description, price, image) and save

### Customer Workflow
1. Browse the product listing on the homepage
2. Click on a product to view details
3. Add products to the cart by specifying quantity
4. Review cart contents, update quantities, or remove items
5. (Note: Checkout functionality is not implemented as per requirements)

## Project Structure

- `models.py`: Contains Product, Cart, and CartItem models
- `views.py`: Contains views for product listing, detail, and cart functionality
- `urls.py`: URL routing configuration
- `admin.py`: Admin panel configuration
- `templates/`: HTML templates for the frontend

## Notes

- This is a simple implementation without user authentication or payment processing
- The project uses session-based cart management
- Bootstrap is used for frontend styling

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).