# Online Market API Documentation

This document provides a comprehensive overview of the Online Market API endpoints. It includes information on managing products and categories, with secure access using JWT authentication.

## Table of Contents

- [Authorization](#authorization)
- [Products](#products)
- [Categories](#categories)
- [General API Information](#general-api-information)

---

## Authorization

All protected endpoints require JWT authentication. Obtain an access token by logging in with the `/api/v1/login/` endpoint. Include this token in the `Authorization` header for all requests requiring authentication.

### Obtain Token
- **POST** `/api/v1/login/`
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
- **POST** `/api/v1/token/refresh/`
  - **Request Body**:
    ```json
    {
      "refresh": "refresh_token"
    }
    ```

Include the access token in the `Authorization` header for all protected endpoints:
Authorization: Bearer access_token

---

## Products

### List All Products
- **GET** `/api/v1/product/`
  - Retrieves a list of all products available in the market.
  - **Authorization**: Not required.

### Retrieve a Single Product
- **GET** `/api/v1/product/{product_id}/`
  - Retrieves detailed information about a specific product.
  - **Authorization**: Not required.

### Create a New Product
- **POST** `/api/v1/product/create/`
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
- **PUT** `/api/v1/product/update/{product_id}/`
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
- **PATCH** `/api/v1/product/update/{product_id}/`
  - **Authorization**: Requires admin privileges.
  - **Request Body** (example):
    ```json
    {
      "price": 1400
    }
    ```

### Delete a Product
- **DELETE** `/api/v1/product/delete/{product_id}/`
  - **Authorization**: Requires admin privileges.

---

## Categories

### List All Categories
- **GET** `/api/v1/categories/`
  - Retrieves a list of all product categories.
  - **Authorization**: Not required.

### Retrieve a Single Category
- **GET** `/api/v1/categories/{category_id}/`
  - Retrieves detailed information about a specific category.
  - **Authorization**: Not required.

### Create a New Category
- **POST** `/api/v1/categories/create/`
  - **Authorization**: Requires admin privileges.
  - **Request Body**:
    ```json
    {
      "name": "Electronics",
      "description": "Electronic devices and gadgets"
    }
    ```

### Update an Existing Category
- **PUT** `/api/v1/categories/update/{category_id}/`
  - **Authorization**: Requires admin privileges.
  - **Request Body**:
    ```json
    {
      "name": "Updated Electronics",
      "description": "All electronic devices"
    }
    ```

### Partially Update a Category
- **PATCH** `/api/v1/categories/update/{category_id}/`
  - **Authorization**: Requires admin privileges.
  - **Request Body** (example):
    ```json
    {
      "description": "New description"
    }
    ```

### Delete a Category
- **DELETE** `/api/v1/categories/delete/{category_id}/`
  - **Authorization**: Requires admin privileges.

---

## General API Information

- **API Base URL**: `http://127.0.0.1:8000/api/v1/`
- All endpoints require HTTP headers to include `"Content-Type: application/json"`.
- For POST, PUT, and PATCH methods, ensure that the request body is a valid JSON object.
  
---