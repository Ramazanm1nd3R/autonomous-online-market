# Online Market API Documentation

This document provides a comprehensive overview of the Online Market API endpoints. It includes information on managing products, categories, and carts, with secure access using JWT authentication.

## Table of Contents

- [Authorization](#authorization)
- [Products](#products)
- [Categories](#categories)
- [Cart](#cart)
- [General API Information](#general-api-information)

---

## Authorization

All protected endpoints require JWT authentication. Obtain an access token by logging in with the `/api/token/` endpoint. Include this token in the `Authorization` header for all requests requiring authentication.

### Obtain Token
- **POST** `/api/token/`
  - **Request Body**:
    ```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```
  - **Response**:
    ```json
    {
      "access": "access_token",
      "refresh": "refresh_token"
    }
    ```

### Refresh Token
- **POST** `/api/token/refresh/`
  - **Request Body**:
    ```json
    {
      "refresh": "refresh_token"
    }
    ```

Include the access token in the `Authorization` header for all protected endpoints:
`Authorization: Bearer access_token`

---

## Products

### List All Products
- **GET** `/api/v1/products/`
  - Retrieves a list of all products available in the market.
  - **Authorization**: Not required.

### Retrieve a Single Product
- **GET** `/api/v1/products/{product_id}/`
  - Retrieves detailed information about a specific product.
  - **Authorization**: Not required.

### Create a New Product
- **POST** `/api/v1/products/create/`
  - **Authorization**: Requires admin privileges.
  - **Request Body**:
    ```json
    {
      "name": "Laptop",
      "description": "High-performance laptop",
      "price": 1500,
      "category": 1
    }
    ```

### Update an Existing Product
- **PUT** `/api/v1/products/update/{product_id}/`
  - **Authorization**: Requires admin privileges.
  - **Request Body**:
    ```json
    {
      "name": "Laptop Pro",
      "description": "Updated high-performance laptop",
      "price": 1600,
      "category": 1
    }
    ```

### Partially Update a Product
- **PATCH** `/api/v1/products/update/{product_id}/`
  - **Authorization**: Requires admin privileges.
  - **Request Body** (example):
    ```json
    {
      "price": 1400
    }
    ```

### Delete a Product
- **DELETE** `/api/v1/products/delete/{product_id}/`
  - **Authorization**: Requires admin privileges.

---

## Categories

### List All Categories
- **GET** `/api/v1/products/categories/`
  - Retrieves a list of all product categories.
  - **Authorization**: Not required.

### Retrieve a Single Category
- **GET** `/api/v1/products/categories/{category_id}/`
  - Retrieves detailed information about a specific category.
  - **Authorization**: Not required.

### Create a New Category
- **POST** `/api/v1/products/categories/create/`
  - **Authorization**: Requires admin privileges.
  - **Request Body**:
    ```json
    {
      "name": "Electronics",
      "description": "Electronic devices and gadgets"
    }
    ```

### Update an Existing Category
- **PUT** `/api/v1/products/categories/update/{category_id}/`
  - **Authorization**: Requires admin privileges.
  - **Request Body**:
    ```json
    {
      "name": "Updated Electronics",
      "description": "All electronic devices"
    }
    ```

### Partially Update a Category
- **PATCH** `/api/v1/products/categories/update/{category_id}/`
  - **Authorization**: Requires admin privileges.
  - **Request Body** (example):
    ```json
    {
      "description": "New description"
    }
    ```

### Delete a Category
- **DELETE** `/api/v1/products/categories/delete/{category_id}/`
  - **Authorization**: Requires admin privileges.

---

## Cart

### View Cart
- **GET** `/api/v1/carts/cart/`
  - Retrieves the contents of the user's cart.
  - **Authorization**: Requires user authentication.

### Add Item to Cart
- **POST** `/api/v1/carts/cart/add/{product_id}/`
  - Adds a specified product to the cart.
  - **Authorization**: Requires user authentication.

### Remove Item from Cart
- **POST** `/api/v1/carts/cart/remove/{item_id}/`
  - Removes a specified item from the cart.
  - **Authorization**: Requires user authentication.

---

## General API Information

- **API Base URL**: `http://127.0.0.1:8000/api/v1/`
- All endpoints require HTTP headers to include `"Content-Type: application/json"`.
- For POST, PUT, and PATCH methods, ensure that the request body is a valid JSON object.

--- 

