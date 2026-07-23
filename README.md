# EBuy Backend

## Tech Stack

* **Framework:** Django & Django REST Framework (DRF)
* **Database:** SQLite (Development) / PostgreSQL compatible
* **Authentication:** JSON Web Tokens (JWT via `djangorestramework-simplejwt`)
* **Filtering & Search:** `django-filter`, DRF Search & Ordering filters

---

## What It's About:

* A robust RESTful backend API built to support the EBuy e-commerce platform.
* Powers secure user registration, token-based authentication, product inventory management, category organization, and automated order processing.
* Features custom seller endpoints, ensuring authenticated users can list, manage, and view their specific product inventory securely.
* Designed with clean modular architecture to seamlessly integrate with modern frontend applications.

---

## How to Use It:

1. Clone the repository and navigate into the backend directory.
2. Create and activate a Python virtual environment:
   python -m venv venv
   source venv/bin/activate
* ** Install the required dependencies: pip install -r requirements.txt
* ** Run database migrations and start the development server:
   python manage.py migrate
   python manage.py runserver

## API Architecture & Features:
* ** User Authentication: Endpoints for user registration, token acquisition, and profile retrieval/updates via JWT.
* ** Product Catalog: List, create, retrieve, update, and delete products with built-in search, ordering, and category filtering. Sellers can manage their exclusive product inventories.
* ** Order Management: Secure endpoints allowing authenticated users to place, view, and track order histories and order items.
* ** Containerization: Ready for deployment using Docker via container build configurations.

  ## Conclusion:
* ** EBuy Backend delivers a secure, highly scalable API foundation capable of managing core e-commerce workflows.
* ** With token-based security and clean modular structuring, it powers seamless integration across full-stack environments.

  ## Licenses:
* ** This project is licensed under the MIT License.

  ## Author
Prince Evanson
