# FastAPI Contacts API

## Overview
This is a FastAPI-based application that provides a RESTful API for managing contacts.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/fastapi-contacts-api.git
   cd fastapi-contacts-api
   ```

2. Ensure that poetry and docker are installed.

3. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

3. Set up the database using Docker:
   ```sh
   docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres
   ```

4. Run the application:
   ```sh
   poetry run main.py
   ```

## API Documentation

### **Contacts Endpoints**

#### 1. Get all contacts
- **Endpoint:** `GET /api/contacts/`
- **Query Parameters:**
  - `skip` (integer, default=0) - Number of records to skip
  - `limit` (integer, min=10, max=100, default=10) - Number of records to return
  - `first_name` (string)
  - `last_name` (string, optional)
  - `email` (string, optional)
- **Response:**
  ```json
  [
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "johndoe@example.com",
      "phone": "+123456789",
      "date_of_birth": "1990-01-01"
    }
  ]
  ```

#### 2. Get a single contact
- **Endpoint:** `GET /api/contacts/{contact_id}`
- **Path Parameter:**
  - `contact_id` (integer) - The ID of the contact to retrieve
- **Response:**
  ```json
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "phone": "+123456789",
    "date_of_birth": "1990-01-01"
  }
  ```

#### 3. Create a new contact
- **Endpoint:** `POST /api/contacts/`
- **Request Body:**
  ```json
  {
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "janedoe@example.com",
    "phone": "+987654321",
    "date_of_birth": "1992-05-15"
  }
  ```
- **Note:** The `phone` field must be **RFC3966 compliant**.
- **Response:**
  ```json
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "janedoe@example.com",
    "phone": "+987654321",
    "date_of_birth": "1992-05-15"
  }
  ```

#### 4. Update a contact
- **Endpoint:** `PUT /api/contacts/{contact_id}`
- **Path Parameter:**
  - `contact_id` (integer) - The ID of the contact to update
- **Request Body:**
  ```json
  {
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "janedoe@example.com",
    "phone": "+987654321",
    "date_of_birth": "1992-05-15"
  }
  ```
- **Response:**
  ```json
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "janedoe@example.com",
    "phone": "+987654321",
    "date_of_birth": "1992-05-15"
  }
  ```

#### 5. Delete a contact
- **Endpoint:** `DELETE /api/contacts/{contact_id}`
- **Path Parameter:**
  - `contact_id` (integer) - The ID of the contact to delete
- **Response:**
  ```json
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "janedoe@example.com",
    "phone": "+987654321",
    "date_of_birth": "1992-05-15"
  }
  ```

### **Additional Endpoints**

#### Get upcoming birthdays
- **Endpoint:** `GET /api/contacts/birthdays`
- **Description:** Returns contacts with birthdays in the next 7 days.
- **Response:**
  ```json
  [
    {
      "id": 3,
      "first_name": "Alice",
      "last_name": "Smith",
      "email": "alice@example.com",
      "phone": "+1122334455",
      "date_of_birth": "1995-02-10"
    }
  ]
  ```

#### Seed contacts data
- **Endpoint:** `POST /api/contacts/seed`
- **Query Parameter:**
  - `count` (integer, default=100) - Number of contacts to generate
- **Response:**
  ```json
  {
    "message": "100 contacts created successfully."
  }
  ```

#### Healthcheck
- **Endpoint:** `GET /api/healthchecker`
- **Description:** Check if the API is connected to database.
- **Response:**
  ```json
  {
    "message": "Database is configured and ready"
  }
  ```

## Documentation
API documentation is available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License
This project is licensed under the MIT License.
