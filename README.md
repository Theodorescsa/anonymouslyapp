# A simple backend system using DJANGO and DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.
## Requirements
- Python 3.11
- Django 5.1.4
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```
## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`/authentication/signin/` | POST | - | Status, Accesstoken and refreshtoken
`/authentication/signup/` | POST | - | Status
-- | -- |-- |--
`/crm/customers/` | GET | READ | Get all customers
`/crm/customers/:id/` | GET | READ | Get a single customer
`/crm/customers/`| POST | CREATE | Create a new customer
`/crm/ustomers/:id/` | PUT | UPDATE | Update a customer
`/crm/customers/:id/` | DELETE | DELETE | Delete a customer
-- | -- |-- |--
`/crm/products/` | GET | READ | Get all products
`/crm/products/:id/` | GET | READ | Get a single product
`/crm/products/`| POST | CREATE | Create a new product
`/crm/products/:id/` | PUT | UPDATE | Update a product
`/crm/products/:id/` | DELETE | DELETE | Delete a product
-- | -- |-- |--
`/crm/employees/` | GET | READ | Get all employees
`/crm/employees/:id/` | GET | READ | Get a single employee
`/crm/employees/`| POST | CREATE | Create a new employee
`/crm/employees/:id/` | PUT | UPDATE | Update a employee
`/crm/employees/:id/` | DELETE | DELETE | Delete a employee
-- | -- |-- |--
`/crm/task-board/` | GET | READ | Get all tasks
`/crm/task-board/:id/` | GET | READ | Get a single task
`/crm/task-board/`| POST | CREATE | Create a new task
`/crm/task-board/:id/` | PUT | UPDATE | Update a task
`/crm/task-board/:id/` | DELETE | DELETE | Delete a task

## Use
We can test the API using [Postman](https://www.postman.com/) or click to swagger doc link: http://43.203.217.22:8000/api-doc/api/schema/swagger-ui

First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
http  http://127.0.0.1:8000/crm/customers/
```
we get:
```
{
    "detail": "Authentication credentials were not provided."
}
```
Instead, if we try to access with credentials:
```
http http://127.0.0.1:8000/crm/customers/1/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxMDcyNDE0LCJpYXQiOjE3MzU4ODg0MTQsImp0aSI6ImU2YTQ3MDI4ZDk2MzRmYmQ5MGEzZjY3ZmRjZDkwYjBmIiwidXNlcl9pZCI6MX0.a6MQjjgJxfpIfY_UzUhJkuiWewfpro60EXziUDRQi9M"
```
we get the movie with id = 1
```
{
  "id": 1,
  "name": "testuser",
  "email": "test@gmail.com",
  "phone": "9999999999999",
  "address": "test",
  "notes": "test"
}
```

## Create users and Tokens

First we need to create a user, so we can log in
```
http POST http://43.203.217.22:8000/authentication/signup/
params:
{
  "username": "testuser",
  "email": "user@gmail.com",
  "password1": "testpassword",
  "password2": "testpassword"
}
```

After we create an account we can login to get a token

To get a token first we need to request
```
http POST http://43.203.217.22:8000/authentication/signin/
params:
{
  "username_login": "admin",
  "password_login": "admin",
  "next": "/dashboard/"
}
```
after that, we get the token
```
{
  "success": true,
  "next_page": "/dashboard/",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNTk3NDgxNCwiaWF0IjoxNzM1ODg4NDE0LCJqdGkiOiIwNGVmODBmMzMxMGE0YmJmYjZjZWNhNjBjOTc3ZWQ5MiIsInVzZXJfaWQiOjF9.KzIQVq9UX7DVxemoQK4gv2NVJHVe6OirlJ9NuXTmr9w",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxMDcyNDE0LCJpYXQiOjE3MzU4ODg0MTQsImp0aSI6ImU2YTQ3MDI4ZDk2MzRmYmQ5MGEzZjY3ZmRjZDkwYjBmIiwidXNlcl9pZCI6MX0.a6MQjjgJxfpIfY_UzUhJkuiWewfpro60EXziUDRQi9M"
}
```
We got two tokens, the access token will be used to authenticated all the requests we need to make, this access token will expire after some time.

The API has some restrictions:
-   Only authenticated users may use these CRUD api

### Request using postman
```
Get all movies
http http://127.0.0.1:8000/api/v1/movies/ "Authorization: Bearer {YOUR_TOKEN}" 
Get a single movie
http GET http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" 
Create a new movie
http POST http://127.0.0.1:8000/api/v1/movies/ "Authorization: Bearer {YOUR_TOKEN}" title="Ant Man and The Wasp" genre="Action" year=2018 
Full update a movie
http PUT http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="AntMan and The Wasp" genre="Action" year=2018
Partial update a movie
http PATCH http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="AntMan and The Wasp" 
Delete a movie
http DELETE http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}"
```

### Pagination
The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page_size={your_page_size_number}
```
http http://127.0.0.1:8000/api/v1/movies/?page=1 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?page=3 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?page=3&page_size=15 "Authorization: Bearer {YOUR_TOKEN}"
```

### Filters
The API supports filtering, you can filter by the attributes of a movie like this
```
http http://127.0.0.1:8000/api/v1/movies/?title="AntMan" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?year=2020 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?year__gt=2019&year__lt=2022 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?genre="Action" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?creator__username="myUsername" "Authorization: Bearer {YOUR_TOKEN}"
```

You can also combine multiples filters like so
```
http http://127.0.0.1:8000/api/v1/movies/?title="AntMan"&year=2020 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/movies/?year__gt=2019&year__lt=2022&genre="Action" "Authorization: Bearer {YOUR_TOKEN}"
```

