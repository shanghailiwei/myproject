def calculate_total_price(price, quantity, discount=0):
    """Function calculate_total_price.

    Description: This function does something.

    Args:
        price (Any): Description of price
    quantity (Any): Description of quantity
    discount (Any): Description of discount

    Returns:
        None: Description of return value.
    """
    total = price * quantity
    if discount > 0:
        total = total * (1 - discount)
    return total

def validate_user_input(username, password, min_length=6):
    """Function validate_user_input.

    Description: This function does something.

    Args:
        username (Any): Description of username
    password (Any): Description of password
    min_length (Any): Description of min_length

    Returns:
        None: Description of return value.
    """
    if len(username) < min_length or len(password) < min_length:
        return False
    return True
