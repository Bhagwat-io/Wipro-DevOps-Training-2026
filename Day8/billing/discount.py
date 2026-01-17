# discount.py
# User Defined Module for applying discount on total bill

def apply_discount(total):
    """Apply discount based on rules"""
    if total >= 1000:
        return total * 0.90     # 10% discount
    elif total >= 500:
        return total * 0.95     # 5% discount
    return total                # No discount
