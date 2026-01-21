# Coffee Order Management API

Backend REST API for managing users, products, and orders for a small coffee business
Built with FastAPI and JWT authentication

This project is designed as a real-world backend service suitable for freelance or production use

---

## Features

- JWT Authentication (Register & Login)
- Role-based access (Admin & User)
- Product management (Admin only)
- Order management with ownership logic
- Secure password hashing
- Clean project structure
- Auto-generated API documentation (Swagger)

---

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite (easy to migrate to PostgreSQL)
- JWT (python-jose)
- Passlib (bcrypt)

```
app/
├── core/
│   ├── config.py        # Configuration
│   └── security.py      # JWT & password hashing
├── database.py          # Database setup
├── models/
│   ├── user.py
│   ├── product.py
│   └── order.py
├── schemas/
│   ├── user.py
│   ├── product.py
│   └── order.py
├── routers/
│   ├── auth.py
│   ├── product.py
│   └── order.py
├── dependencies.py      # Dependency injection
└── main.py              # FastAPI app
```

---

## Setup

### 1. Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Server

```bash
uvicorn app.main:app --reload
```

Server will start at `http://localhost:8000`

---

## API Documentation

Auto-generated docs available at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Authentication

### Register

```http
POST /auth/register

{
  "email": "[EMAIL_ADDRESS]",
  "password": "password123"
}
```

### Login

```http
POST /auth/login

{
  "email": "[EMAIL_ADDRESS]",
  "password": "password123"
}
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Protected Routes

Add `Authorization: Bearer <token>` header to all protected endpoints.


## Products (Admin Only)

### List Products

```http
GET /products/
Authorization: Bearer <token>
```

### Create Product

```http
POST /products/
Authorization: Bearer <token>

{
  "name": "Latte",
  "price": 4.50
}
```

### Update Product

```http
PUT /products/{id}
Authorization: Bearer <token>

{
  "name": "Latte",
  "price": 4.75
}
```

### Delete Product

```http
DELETE /products/{id}
Authorization: Bearer <token>
```

---

## Orders

### Create Order

```http
POST /orders/
Authorization: Bearer <token>

{
  "product_id": 1,
  "quantity": 2
}
```

### List Orders

```http
GET /orders/
Authorization: Bearer <token>
```

- **Admin**: View all orders
- **User**: View only own orders

---

## Production Readiness

This project is production-ready:

- JWT authentication with proper expiration
- Role-based access control
- Password hashing (bcrypt)
- Clean separation of concerns
- Proper error handling
- Structured database models (SQLAlchemy)
- Environment variable support (in `app/core/config.py`)

---

## Deployment

To deploy to production:

1. Replace SQLite with PostgreSQL
2. Add proper environment variables
3. Use Gunicorn + Uvicorn for production
4. Add HTTPS
5. Implement rate limiting
6. Add proper logging

---

## Contributing

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request

---

## License

This project is open source and available under the MIT License.

---

## Author

**Irham Rizqan**

- GitHub: [IrhamRizqan](https://github.com/IrhamRizqan)
- LinkedIn: [irhamrizqanz](https://www.linkedin.com/in/irhamrizqanz/)

---

## Acknowledgments

- FastAPI team for the amazing framework
- SQLAlchemy community for the ORM
- All open-source contributors

---

## Support

If you need help or have questions, feel free to:

- Open an issue
- Submit a pull request
- Contact me directly

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload

# Access docs
http://localhost:8000/docs
```