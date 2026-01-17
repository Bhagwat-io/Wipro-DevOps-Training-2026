# billing.py
# User Defined Module for calculating bill amounts

def calculate_total_price(price, qty):
    """Returns total = price × quantity"""
    return price * qty

def generate_bill_item(item, price, qty):
    """Returns formatted bill line"""
    total = calculate_total_price(price, qty)
    return f"{item} (Qty: {qty}) → Rs.{total}"
def addition(a,b):
    return a+b
