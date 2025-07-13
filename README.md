



# 🛒 Product Review API – Django REST Framework

This is a backend REST API project to manage products and their reviews with role-based access (Admin & Regular users),
 built as a technical assignment for **Pfactorial Technologies**.

---

## 🚀 Features

✅ User Registration & Token-based Login  
✅ Logout API  
✅ Admin can manage Products (CRUD)  
✅ Regular Users can post one Review per Product  
✅ Duplicate reviews blocked  
✅ Ratings strictly between 1 and 5  
✅ Product average rating auto-calculated  
✅ Admin can view all registered users  
✅ Token Authentication via DRF  
✅ Clean nested endpoints with DRF routers

---

## ⚙️ Tech Stack

- Python 3.x
- Django 4.x / 5.x
- Django REST Framework
- Token Authentication
- SQLite (default)

---

## 🧱 Project Structure
```

product-review-api/
├── product_review_system/     # Django project folder
│   |── settings.py
|   |── urls.py
├── reviews/                   # Django app for reviews
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   └── urls.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

```





---

## 🔐 API Endpoints

### ✅ Authentication

```

| Method | Endpoint              | Description                     |
|--------|-----------------------|---------------------------------|
| POST   | `/api/auth/register/` | Register a new user             |
| POST   | `/api/auth/login/`    | Login and receive auth token    |
| POST   | `/api/auth/logout/`   | Logout (delete token)           |
| GET    | `/api/auth/users/`    | Admin only – list all users     |

### 📦 Product Operations

| Method     | Endpoint              | Description                     |
|------------|-----------------------|---------------------------------|
| GET        | `/api/products/`      | List all products               |
| POST       | `/api/products/`      | Create product (admin only)     |
| GET        | `/api/products/<id>/` | Retrieve product details        |
| PUT/PATCH  | `/api/products/<id>/` | Update product (admin only)     |
| DELETE     | `/api/products/<id>/` | Delete product (admin only)     |

### ✍️ Product Reviews (Nested)

| Method | Endpoint                            | Description                       |
|--------|-------------------------------------|-----------------------------------|
| GET    | `/api/products/<id>/reviews/`       | List all reviews for a product    |
| POST   | `/api/products/<id>/reviews/`       | Submit review (regular users only)|

---
```
## 📌 Authentication Header

After login, use this header for protected endpoints:

```

Authorization: Token (your_token_here)

````

---

## 🛠️ How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/product-review-api.git
cd product-review-api
````

### 2. Create virtual environment

```bash
python -m venv env
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/api/`

---

## 🧪 Example: Register, Login, Review (Postman)

### Register

```
POST /api/auth/register/
{
  "username": "ashif",
  "email": "ashif@example.com",
  "password": "yourpassword"
}
```

### Login

```
POST /api/auth/login/
{
  "username": "ashif",
  "password": "yourpassword"
}
→ Response: { "token": "..." }
```

### Header for Auth APIs

```
Authorization: Token your_token_here
```

---

## 👤 User Roles

| Role    | Access                            |
| ------- | --------------------------------- |
| Admin   | Full product CRUD, view all users |
| Regular | View + Review products            |

---

## 🎁 Notes

* Only one review per user per product
* Rating must be between 1 and 5
* All users can view products and reviews
* Token Auth ensures secure API calls
* Admin-only protected routes are enforced

---

## 🧑‍💻 Assignment By

> **Pfactorial Technologies**
> Role: Backend Developer – Technical Assignment

---

## ✅ Author

Made with ❤️ by [Ashif Aachi]





