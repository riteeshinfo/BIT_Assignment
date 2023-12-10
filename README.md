# Task Management System API

This project implements a RESTful API for a task management system using Django Rest Framework.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [List all tasks](#list-all-tasks)
  - [Retrieve a single task by ID](#retrieve-a-single-task-by-id)
  - [Create a new task](#create-a-new-task)
  - [Update an existing task](#update-an-existing-task)
  - [Delete a task](#delete-a-task)
- [Authentication](#authentication)
- [Permissions](#permissions)
- [Unit Tests](#unit-tests)
- [Documentation](#documentation)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/task-management-api.git
    cd task-management-api
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the admin panel at `http://127.0.0.1:8000/admin/` to add tasks and manage users.

## API Endpoints

### List all tasks

- Endpoint: `/api/`
- Method: GET
- Authentication: Token-based authentication required

### Retrieve a single task by ID

- Endpoint: `/api/<int:pk>/`
- Method: GET
- Authentication: Token-based authentication required

### Create a new task

- Endpoint: `/api/add/`
- Method: POST
- Authentication: Token-based authentication required

### Update an existing task

- Endpoint: `/api/update/<int:pk>/`
- Method: POST
- Authentication: Token-based authentication required
- Permissions: Users can only update their own tasks

### Delete a task

- Endpoint: `/api/delete/<int:pk>/`
- Method: DELETE
- Authentication: Token-based authentication required
- Permissions: Users can only delete their own tasks

## Authentication

Token-based authentication is implemented for the API. To authenticate, include the token in the Authorization header of your requests:

```http
Authorization: Token your_token_here

## UnitTest
python manage.py test tasks

