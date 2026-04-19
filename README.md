Restaurant Ordering System (Python Console App)

A simple **Python-based restaurant management system** that allows users to view a menu, place orders, generate order numbers, calculate bills, and print receipts.

This project simulates a real-world **Point of Sale (POS) system** for a restaurant.

---

##  Features

- Display restaurant main menu
- Place food and drink orders
- Generate random order numbers
- Calculate total bill automatically
- Print detailed receipt
- Input validation (only valid menu items allowed)
- Loop-based menu system (runs until exit)

---

## Concepts Used

This project demonstrates:
- Python dictionaries (nested data structures)
- Functions
- Loops (`while`, `for`)
- Conditional statements (`if/elif/else`)
- Input validation
- Random number generation
- Modular programming

---

## Project Structure

```python
mydict → Stores full restaurant menu (meals, drinks, extras, desserts + prices)

mainmenu() → Displays welcome message

place_order(menu) → Allows user to select valid menu items

order_num() → Generates random order number

calculation(order, menu) → Calculates total bill

print_receipt(order, menu, order_number) → Prints formatted receipt

Main loop → Controls system navigation
Menu System

The menu includes:

Meals
Breakfast
Lunch
Dinner
Drinks
Hot drinks
Cold drinks
Alcoholic drinks
Desserts
Ice cream
Cakes
Local specials
Extras
Sauces
Add-ons
How to Run
1. Clone the repository
git clone https://github.com/your-username/restaurant-system.git
2. Navigate into the project
cd restaurant-system
3. Run the program
python function.py
Example Usage
1. Main menu
2. Order
3. Bill
4. Receipt
5. Exit
Sample Output:
Your order number is: 45231
Your order is: ['Beef Burger', 'Coke']

TOTAL: R100
Sample Receipt
==============================
     TEEKAY SMALL KITCHEN
==============================
Order Number: 45231

Beef Burger              R80
Coke                     R20

------------------------------
TOTAL:                   R100
==============================
Thank you for visiting!

Give it a star ⭐ and feel free to improve it!




