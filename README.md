# Ecommerce Backend

## Prerequisites

- Python 3.12+
- PostgreSQL
- Redis
- uv

---

## Installation

Clone the repository:

```bash
git clone git@github.com:Chinmay-Jadhav/Ecommerce.git
cd Ecommerce
```

Create and install dependencies:

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=your-secret-key

JWT_ACCESS_TOKEN_MINUTES=int
JWT_REFRESH_TOKEN_DAYS=int

DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

BASE_URL = "http://127.0.0.1:8000"
```

---

## Apply Migrations

```bash
uv run python manage.py migrate
```

Default payment methods are automatically loaded through Django data migrations.

---

## Create Superuser

```bash
uv run python manage.py createsuperuser
```

---

## Run the Services

### Django

```bash
uv run python manage.py runserver
```

### Redis

```bash
redis-server
```

### Celery Worker

```bash
uv run celery -A ecommerce worker -l INFO --pool=solo
```

### Flower (Optional)

```bash
uv run celery -A ecommerce flower
```

Flower Dashboard:

```
http://localhost:5555
```


---

## Testing the API

You can use **Postman** or any API development tool (e.g. Insomnia, Bruno) to test the endpoints.

### 1. Register a User

```
POST /api/v1/auth/register/

{
    "username": "<username>",
    "email": "<user@email.com>",
    "password": "<pwd>",
    "confirm_password": "<pwd>"
}
```

### 2. Login

```
POST /api/v1/auth/login/

{
    "username": "<username>",
    "password": "<pwd>"
}
```

Copy the returned **access token**.

### 3. Authorize Requests

Add the following header for authenticated endpoints:

```
Authorization: Bearer <access_token>
```

> **Note:** Ensure at least one Product and one Payment Method exist before creating an order.

### 4. Create an Order

```
POST /api/v1/orders/
```

Example request body:

```json
{
    "product": 1,
    "payment_method": 1,
    "quantity": 2
}
```

The response contains a `gateway_order_id`.
Save the returned `gateway_order_id` ; it is required when testing the callback endpoint.

### 5. Simulate Payment Gateway Callback

```
POST /api/v1/payment-gateway/callback/
```

Example request body:

```json
{
    "gateway_order_id": "<gateway_order_id>",
    "payment_transaction_id": "PAY-123456789",
    "signature": "dummy-signature",
    "status": "SUCCESS"
}
```

Replace `<gateway_order_id>` with the value returned when creating the order.

> **Note:** The payment gateway callback does not require JWT authentication because it simulates a callback from an external payment provider.

### 6. Verify Order Status

```
GET /api/v1/orders/<order_id>/
```

The order should now contain:

- Updated `status`
- `gateway_order_id`
- `payment_transaction_id`
- `payment_completed_at`