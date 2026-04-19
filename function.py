import random 


mydict = {
        "restaurant_info": {
            "name": "Urban Bites",
            "location": "Johannesburg, South Africa",
            "opening_hours": "09:00 - 22:00",
            "contact": "+27 11 555 7890"
        },

        "meals": {
            "breakfast": {
                "Eggs & Toast": 35,
                "Pancakes": 45,
                "Full English Breakfast": 85,
                "Omelette": 40,
                "Breakfast Burrito": 60
            },

            "lunch": {
                "Beef Burger": 80,
                "Chicken Wrap": 65,
                "Veggie Salad": 55,
                "Grilled Chicken & Rice": 90,
                "Fish & Chips": 85
            },

            "dinner": {
                "Steak & Chips": 120,
                "BBQ Ribs": 140,
                "Spaghetti Bolognese": 95,
                "Chicken Curry": 110,
                "Grilled Salmon": 150
            }
        },

        "drinks": {
            "hot": {
                "Coffee": 25,
                "Cappuccino": 30,
                "Tea": 20,
                "Hot Chocolate": 28
            },

            "cold": {
                "Coke": 20,
                "Sprite": 20,
                "Fanta": 20,
                "Still Water": 15,
                "Sparkling Water": 18
            },

            "alcoholic": {
                "Corona": 35,
                "Heineken": 38,
                "Savanna": 30,
                "Jack Daniels": 45,
                "Red Wine": 50
            }
        },

        "extras": {
            "sauces": {
                "Barbecue Sauce": 10,
                "Garlic Mayo": 10,
                "Peri-Peri Sauce": 12,
                "Sweet Chilli": 10,
                "Cheese Sauce": 15
            },

            "add_ons": {
                "Extra Cheese": 15,
                "Extra Bacon": 25,
                "Extra Chicken": 30,
                "Mushrooms": 12,
                "Avocado": 20
            }
        },

        "desserts": {
            "ice_cream": {
                "Vanilla": 25,
                "Chocolate": 25,
                "Strawberry": 25,
                "Mint Chocolate": 28
            },

            "cakes": {
                "Chocolate Cake": 40,
                "Cheesecake": 45,
                "Red Velvet": 50,
                "Carrot Cake": 45
            },

            "local_specials": {
                "Malva Pudding": 35,
                "Koeksisters": 20,
                "Milk Tart": 30
            }
        },

        "special_offers": {
            "daily_special": "Buy 1 Burger, Get Free Fries",
            "weekend_deal": "2 Cocktails for the price of 1",
            "student_discount": "10% off with student card",
            "family_combo": "R199 Family Meal Deal"
        },

        "ratings": {
            "google": 4.5,
            "tripadvisor": 4.3,
            "facebook": 4.6
        }
    }

   
def mainmenu():
    print("WELCOME TO TEEKAY SMALL KITCHEN")

    
def place_order(menu):

    # collect all valid items from dictionary
    valid_items = []

    for category in menu["meals"].values():
        valid_items.extend(category.keys())

    for category in menu["drinks"].values():
        valid_items.extend(category.keys())

    for category in menu["extras"].values():
        valid_items.extend(category.keys())

    for category in menu["desserts"].values():
        valid_items.extend(category.keys())

    order = []

    while True:
        item = input("Add item (type 'done' to finish): ")

        if item.lower() == "done":
            break

        if item in valid_items:
            order.append(item)
            print(f"{item} added to order")
        else:
            print("Item not on menu ")

    return order

def order_num():
    return random.randint(1,100000)

def calculation(order, menu):

    total = 0

    for item in order:

        for category in menu["meals"].values():
            if item in category:
                total += category[item]

        for category in menu["drinks"].values():
            if item in category:
                total += category[item]

        for category in menu["extras"].values():
            if item in category:
                total += category[item]

        for category in menu["desserts"].values():
            if item in category:
                total += category[item]

    return total

def print_receipt(order, menu, order_number):

    print("\n" + "="*30)
    print("        TEEKAY SMALL KITCEN")
    print("="*30)
    print(f"Order Number: {order_number}\n")

    total = 0

    for item in order:
        price = None

        for category in menu["meals"].values():
            if item in category:
                price = category[item]

        for category in menu["drinks"].values():
            if item in category:
                price = category[item]

        for category in menu["extras"].values():
            if item in category:
                price = category[item]

        for category in menu["desserts"].values():
            if item in category:
                price = category[item]

        if price is not None:
            print(f"{item:<25} R{price}")
            total += price
        else:
            print(f"{item:<25} NOT FOUND")

    print("\n" + "-"*30)
    print(f"TOTAL:               R{total}")
    print("="*30)
    print("Thank you for visiting Urban Bites!")

    
while True:
    
    print("1. Main menu")
    print("2. Order")
    print("3. Bill")
    print("4. RECEIPT")
    print("5. EXIT")
    
    choice = int(input("Enter a number between 1 and 4: "))
    if choice< 1 or choice > 5:
        print("Please try again")
        continue
  
    if choice == 1:
        mainmenu()
        
    elif choice == 2:
        order = place_order(mydict)
        number = order_num()
        print(f"Your order number is: {number}")
        print(f"Your order is: {order}")

    elif choice == 3:
        total = calculation(order, mydict)
        print(f"Your bill total is: {total}")

    elif choice == 4:
        order = place_order(mydict)
        number = order_num()
        print_receipt(order, mydict, number)

    elif choice == 5:
        print("Thank you for visiting")
        break
    
    
    





            
   
    


