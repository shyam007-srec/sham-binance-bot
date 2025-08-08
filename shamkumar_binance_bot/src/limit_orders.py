# src/limit_orders.py

import sys
from datetime import datetime

def place_limit_order(symbol, side, quantity, price):
    order_id = f"LO-{datetime.now().strftime('%H%M%S')}"
    message = (f"{datetime.now()} | LIMIT ORDER | {symbol} | {side} | Qty: {quantity} "
               f"| Price: {price} | Order ID: {order_id}")
    print(message)
    log_action(message)
    return {"order_id": order_id, "status": "simulated"}

def log_action(message):
    with open("bot.log", "a") as f:
        f.write(message + "\n")

def validate_input(args):
    if len(args) != 5:
        print("Usage: python limit_orders.py <SYMBOL> <SIDE> <QUANTITY> <PRICE>")
        sys.exit(1)
    
    symbol = args[1].upper()
    side = args[2].upper()

    try:
        quantity = float(args[3])
        price = float(args[4])
        if quantity <= 0 or price <= 0:
            raise ValueError
    except ValueError:
        print("Quantity and price must be positive numbers.")
        sys.exit(1)

    if side not in ["BUY", "SELL"]:
        print("Side must be either BUY or SELL.")
        sys.exit(1)

    return symbol, side, quantity, price

if __name__ == "__main__":
    symbol, side, quantity, price = validate_input(sys.argv)
    place_limit_order(symbol, side, quantity, price)
