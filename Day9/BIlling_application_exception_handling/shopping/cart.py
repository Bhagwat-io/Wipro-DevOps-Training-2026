from shopping.validator import ( validate_item,validate_price,validate_qty,validate_discount)

def caluculate_total(price,qty,discount):
    validate_price(price)
    validate_qty(qty)
    validate_discount(discount)
    total= price * qty
    discount_amount=total * (discount/100)
    final_amount=total-discount_amount
    return total,discount_amount,final_amount
