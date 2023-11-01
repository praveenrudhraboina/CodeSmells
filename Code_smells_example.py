def calculate_total_price(items):
    total = 0
    for item in items:
        total += calculate_item_price(item)
    return total

def calculate_item_price(item):
    if item.quantity > 0:
        return calculate_discounted_price(item.price)
    else:
        return 0

def calculate_discounted_price(price):
    if price > 100:
        return price * 0.9
    else:
        return price * 0.95
