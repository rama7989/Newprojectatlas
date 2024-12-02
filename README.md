# Project Atlas

## Decription

The Django Project Atlas API is a RESTful web service designed to manage a films, inventory, customers, films, and related entities. 
It provides endpoints for CRUD (Create, Read, Update, Delete) operations on various models, enabling efficient management of store data.

## Features

Manage actors, films, categories, customers, payment,rentals and more.
Support for authentication using JWT tokens.
Comprehensive testing suite using pytest.

##Installation Requirements

####Prerequisites
Python 3.11 
Django 5.1.3 
Django REST Framework
Djangorestframework-simplejwt
PostgreSQL
Postman

##Steps to Set Up the Project
### 1.Clone the Repository:

git clone https://github.com/rama7989/Newprojectatlas.git

cd Newprojectatlas

2. Create a Virtual Environment:

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Install Dependencies:

pip install -r requirements.txt

4.Configure the Database: 

Update the DATABASES setting in settings.py to match your database configuration.In this project we used Postgresql

5.Run Migrations:

python manage.py migrate

6. Create a Superuser:

python manage.py createsuperuser

7.Run the Development Server:

python manage.py runserver

##Api Endpoints:

  http://127.0.0.1:8000/

   "actors": "http://127.0.0.1:8000/actors/",
   
  "address": "http://127.0.0.1:8000/address/",
    
  "category": "http://127.0.0.1:8000/category/",
    
  "city": "http://127.0.0.1:8000/city/",
  
  "country": "http://127.0.0.1:8000/country/",
  
  "customer": "http://127.0.0.1:8000/customer/",
  
   "films": "http://127.0.0.1:8000/films/",
   
  "filmactor": "http://127.0.0.1:8000/filmactor/",
    
  "fcategory": "http://127.0.0.1:8000/fcategory/",
    
  "inventory": "http://127.0.0.1:8000/inventory/",
    
  "language": "http://127.0.0.1:8000/language/",
    
  "payment": "http://127.0.0.1:8000/payment/",
    
  "rental": "http://127.0.0.1:8000/rental/",
    
  "staff": "http://127.0.0.1:8000/staff/",
    
  "store": "http://127.0.0.1:8000/store/"
    

##Get the list of actors by following below steps in  Postman:

  #### List Actors
  
  URL: http://127.0.0.1:8000/actors/
  
  Method: GET / POST / DELETE / PUT
  
  Authentication: Bearer Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
                                 eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMzMTc3MTY3LCJpYXQiOjE3MzI4NzcxNjcsImp0aSI6Ijc1YWE1NzdhNWMyYzQ1NDY4NDgzM2I5ODVlMzkyYzRmIiwidXNlcl9pZCI6Mn0.
                                 TEoUkVZfvve4-uvE-p1KvTmy6G5qb4Cakc_iWta2D9k
                                 
We can follow same steps for every models to perform GET,POST,PUT and DELETE operations
