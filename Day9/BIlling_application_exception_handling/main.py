from shopping.cart import caluculate_total
from shopping.validator import validate_item


print("\n ================online shoping====")
try:
    name= input("enter the Item name")
    validate_item(name)
    price = float(input("enter price"))
    qty= int(input("enter Quantity"))
    discount=float(input("enter the discount % (0-50):"))
    total,discount_amt,final= caluculate_total(price,qty,discount)
except ValueError as ve:
    print("Error",ve)
except Exception  as e :
    print("Unknown error ",e)
else:
    print("\n ==============bill summery ====")
    print(f"Item: {name}")
    print(f"Total: {total}")
    print(f"Discount Amount: {discount_amt}")
    print(f"final payable : {final}")
finally:
    print("thank you for shopping with us ")
    
