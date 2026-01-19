def validate_item(name):
    if len(name.strip()) == 0:
        raise ValueError("item name can not be empty")
def validate_price(price):
    if price<= 0:
        raise ValueError("price mnuatt be greater than 0")
def validate_qty(qty):
    if qty<=0:
        raise ValueError("Quantity must be greater than 0")
def validate_discount(discount):
    if discount < 0 or discount >50:
        raise ValueError("Discount must be between 0% and 50%")

        