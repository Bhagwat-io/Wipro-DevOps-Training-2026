# main.py
# Importing user-defined modules

import billing
import discount

cart = []

# Taking input for 3 items
for i in range(3):
    print("\nEnter Item", i+1)
    item = input("Item name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    
    line = billing.generate_bill_item(item, price, qty)
    cart.append((item, billing.calculate_total_price(price, qty)))
    print("Added:", line)

# Calculate total bill
total = sum(amount for item, amount in cart)
print("\nTotal before discount:", total)

# Apply discount
final_amount = discount.apply_discount(total)

print("Final Amount to Pay:", final_amount)
