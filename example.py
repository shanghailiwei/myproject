def calculate_total_price(price, quantity, discount=0):
    total = price * quantity
    if discount > 0:
        total = total * (1 - discount)
    return total

def validate_user_input(username, password, min_length=6):
    if len(username) < min_length or len(password) < min_length:
        return False
    return True
