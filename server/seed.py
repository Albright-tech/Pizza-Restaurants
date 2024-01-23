from app import app, db
from models import Restaurant, Pizza, RestaurantPizza
import random

ke_restaurants = [
     "Al-Beik Restaurant",
    "Java House",
    "Artcaffe",
    "Cafe Deli",
    "Kilimanjaro Jamia",
    "Villa Rosa Kempinski",
    "Carnivore Restaurant",
    "Talisman Restaurant",
    "Mama Nitilie Restaurant",
    "Nyama Kafry",
    "Habesha Restaurant",
    "The Talisman",
    "Mama Rocks Gourmet Burgers",
    "About Thyme Restaurant",
    "Cafe Maghreb",
    "Lord Erroll Gourmet Restaurant",
    "Que Pasa Bar & Bistro",
    "Sankara Nairobi, Sarabi Rooftop Bar",
    "Anghiti Restaurant",
    "Seven Seafood & Grill",
    "Zen Garden",
    "Hashmi BBQ",
    "Le Palanka",
    "Hash Grill Restaurant",
    "Camel's Joint",
    "Poppy Pine Joint"
]

pizza_flavors = [
      "Margherita",
    "Pepperoni",
    "Hawaiian",
    "Supreme",
    "BBQ Chicken",
    "Veggie Supreme",
    "Meat Lovers",
    "Buffalo Chicken",
    "Mushroom and Swiss",
    "White Garlic",
    "Pesto and Tomato",
    "Four Cheese",
    "Spinach and Feta",
    "Sausage and Peppers",
    "Mediterranean",
    "BBQ Pulled Pork",
    "Shrimp Scampi",
    "Taco Pizza",
    "Alfredo Chicken",
    "BLT Pizza",
    "Philly Cheesesteak",
    "Caprese",
    "Greek Pizza",
    "Breakfast Pizza",
    "Truffle and Mushroom"
]

def get_random_ingredients():
    pizza_ingredients = [
        "Tomato sauce", "Cheese", "Mushrooms", "Pepperoni", "Onions",
        "Bell peppers", "Olives", "Bacon", "Sausage", "Ham",
        "Pineapple", "Chicken", "Garlic", "Spinach", "Feta cheese",
        "Parmesan cheese", "Oregano",
    ]
    return random.sample(pizza_ingredients, random.randint(3, 10))

def seed_data():
    with app.app_context():
        db.create_all()

        # Create restaurants
        for restaurant_name in ke_restaurants:
            existing_restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
            if not existing_restaurant:
                restaurant = Restaurant(name=restaurant_name, address=f"{restaurant_name} Address")
                db.session.add(restaurant)
        db.session.commit()

        # Create pizzas
        for pizza_flavor in pizza_flavors:
            pizza_ingredients = get_random_ingredients()
            pizza = Pizza(name=pizza_flavor, ingredients=f"{', '.join(pizza_ingredients)}")
            db.session.add(pizza)
        db.session.commit()

        # Create restaurant-pizza associations with prices
        for restaurant_name in ke_restaurants:
            restaurant = Restaurant.query.filter_by(name=restaurant_name).first()
            for pizza_flavor in pizza_flavors:
                pizza = Pizza.query.filter_by(name=pizza_flavor).first()
                price = round(random.uniform(5, 25), 2)  # Random price between 5 and 25
                association = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)
                db.session.add(association)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
