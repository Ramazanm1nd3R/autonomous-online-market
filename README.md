# API Endpoints for Online Market

This document outlines all the API endpoints available in the Online Market application. Each endpoint is designed to provide specific functionality needed for a comprehensive online shopping experience.

## Products

### List all products
- **GET** `/api/v1/products/`
  - Retrieves a list of all products available in the market.

### Retrieve a single product
- **GET** `/api/v1/products/{product_id}/`
  - Retrieves detailed information about a specific product.

### Create a new product
- **POST** `/api/v1/products/create/`
  - Creates a new product. Request must include product name, description, price, and category ID.

### Update an existing product
- **PUT** `/api/v1/products/update/{product_id}/`
  - Fully updates an existing product. All product fields must be provided.

### Partially update a product
- **PATCH** `/api/v1/products/update/{product_id}/`
  - Partially updates an existing product. Only the fields to be updated need to be provided.

### Delete a product
- **DELETE** `/api/v1/products/delete/{product_id}/`
  - Deletes a specific product.

## Categories

### List all categories
- **GET** `/api/v1/categories/`
  - Retrieves a list of all product categories.

### Retrieve a single category
- **GET** `/api/v1/categories/{category_id}/`
  - Retrieves detailed information about a specific category.

### Create a new category
- **POST** `/api/v1/categories/create/`
  - Creates a new category. Request must include category name and description.

### Update an existing category
- **PUT** `/api/v1/categories/update/{category_id}/`
  - Fully updates an existing category. All category fields must be provided.

### Partially update a category
- **PATCH** `/api/v1/categories/update/{category_id}/`
  - Partially updates an existing category. Only the fields to be updated need to be provided.

### Delete a category
- **DELETE** `/api/v1/categories/delete/{category_id}/`
  - Deletes a specific category.

## General API Information

- **API Base URL**: `http://127.0.0.1:8000/api/v1/`
- All endpoints require HTTP headers to include `"Content-Type: application/json"`.
- For POST, PUT, and PATCH methods, ensure that the request body is a valid JSON object.

