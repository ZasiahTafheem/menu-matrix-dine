# Grouped restaurant menu with categories and specific items
menu = {
    "coffee": {
        "cappuccino": 45,
        "latte": 40,
        "espresso": 35
    },
    "burger": {
        "beef burger": 250,
        "crispy chicken burger": 220,
        "veggie burger": 180
    },
    "fruitjuice": {
        "orange juice": 100,
        "apple juice": 120
    },
    "icecream": {
        "vanilla icecream": 75,
        "chocolate icecream": 85
    },
    "pizza": {
        "margherita pizza": 350,
        "pepperoni pizza": 400
    },
    "sandwich": {
        "club sandwich": 150,
        "cheese sandwich": 120
    }
}

print("Welcome to our Restaurant")
print("Please see our menu items which you can order:")
print("******************** MENU ********************")

# Beautifully display grouped categories and items
for category, items in menu.items():
    print(f"\n--- {category.upper()} ---")
    for item, price in items.items():
        print(f"  * {item.title()}: {price} Tk")
        
print("**********************************************")
print("Enter 'no order' to finish and close your order.\n")

# Dictionary to track customer's order: { "item_name": quantity }
customer_order = {}
totcost = 0     

while True:  
    userchoice = input("Enter the specific food name you want to order: ").lower().strip()
    #item_count = int(input("Enter number of item: "))
    if userchoice == "no order": 
         print("Watch out Your order Summary")
         break
    # Check if the ordered item exists inside any of the categories
    found_item = False
    for category, items in menu.items():
        if userchoice in items:
            item_price = items[userchoice]
            found_item = True
            item_count = (input("Enter number of items in digit only like 1,2,3,..: "))
            if item_count.isdigit ():
                customer_count=int(item_count)
            #totcost=item_count*item_price
                totcost += customer_count*item_price

            # Record the number of items ordered
                if userchoice in customer_order:
                   customer_order[userchoice] += customer_count
                else:
                   customer_order[userchoice] = customer_count
                print(f"Success! Added to order: {userchoice.title()} [{customer_count} nos.] (@{item_price} Tk)\n")
            else:
                print("Enter a valid  whole number like 1,2,3,")
            break # Exit the category loop once found
    
    if not found_item:
        print("Sorry! That specific item is not available. Please type the exact name from the menu.\n")
    

    # --- FINAL RECEIPT PRINTING ---
print("\n=================== YOUR RECEIPT ===================")
print(f"{'Qty':<5} | {'Item Name':<25} | {'Unit Price':<10} | {'Total':<10}")
print("-" * 52)

for item_name, customer_count in customer_order.items():
    # Find the unit price again for the receipt breakdown
    unit_price = 0
    for category, items in menu.items():
        if item_name in items:
            unit_price = items[item_name]
            break
    item_total = unit_price * customer_count
    print(f"{customer_count:<5} | {item_name.title():<25} | {unit_price:<10} | {item_total:<10}")
        
print("====================================================")
print(f"Your grand total cost is: {totcost} Tk")
print("Thank you for visiting our restaurant!")
            
        