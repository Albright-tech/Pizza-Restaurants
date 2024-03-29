# Pizza-Restaurants
Pizza Restaurants REST API
Flask Code Challenge - Pizza Restaurants REST API for a Pizza Restaurant domain.

Setup Requirements
Visual Studio Code, see here
Any supported OS / environments / Windows Subsystem for Linux (WSL), details here
Git and Github
Python (Recommend version 3.10+), get the latest here
Pipenv, a Python virtualenv management tool, see details here
Installation
Clone/Download the code from the repository, navigate to the directory on the terminal
Run pipenv install to install required packages
Run pipenv shell to enter the created project environment
Create sample data and test output, run cd app, in the app directory run python app.py to start the API
Language(s)
Python
Endpoints include:
The endpoints are set to the following routes, each endpoint returns JSON data in the format specified along with the appropriate HTTP verb.

GET /restaurants
Returns JSON data in the format below:

[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
GET /restaurants/:id
If the Restaurant exists, JSON data is returned in the format below:

{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
If the Restaurant does not exist, the following JSON data, along with the appropriate HTTP status code is returned:

{
  "error": "Restaurant not found"
}
DELETE /restaurants/:id
If the Restaurant exists, it is removed from the database, along with any RestaurantPizzas that are associated with it

After deleting the Restaurant, an empty response body, along with the appropriate HTTP status code will be returned.

If the Restaurant does not exist, return the following JSON data, along with the appropriate HTTP status code:

{
  "error": "Restaurant not found"
}
GET /pizzas
Returns JSON data in the format below:

[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
POST /restaurant_pizzas
This route creates a new RestaurantPizza that is associated with an existing Pizza and Restaurant. It accepts following properties in the body of the request:

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
When the RestaurantPizza has been created successfully, the following response with the data related to the Pizza is sent back:

{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
If the RestaurantPizza is not created successfully, the following JSON data, along with the appropriate HTTP status code is returned:

{
  "errors": ["validation errors"]
}
Validations
RestaurantPizza Model validation:

Must have a price between 1 and 30
Restaurant Model validation:

Must have a name less than 50 words in length
Must have a unique name
Author
Albright Muchori