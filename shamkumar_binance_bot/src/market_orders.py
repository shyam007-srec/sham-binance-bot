# src/market_orders.py

import sys
from datetime import datetime

def place_market_order(symbol, side, quantity):
    # Simulate market order logic
    order_id = f"MO-{datetime.now().strftime('%H%M%S')}"
    message = f"{datetime.now()} | MARKET ORDER | {symbol} | {side} | Qty: {quantity} | Order ID: {order_id}"
    print(message)
    log_action(message)
    return {"order_id": order_id, "status": "simulated"}

def log_action(message):
    with open("bot.log", "a") as f:
        f.write(message + "\n")

def validate_input(args):
    if len(args) != 4:
        print("Usage: python market_orders.py <SYMBOL> <SIDE> <QUANTITY>")
        sys.exit(1)
    
    symbol = args[1].upper()
    side = args[2].upper()
    try:
        quantity = float(args[3])
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Quantity must be a positive number.")
        sys.exit(1)

    if side not in ["BUY", "SELL"]:
        print("Side must be either BUY or SELL.")
        sys.exit(1)

    return symbol, side, quantity

if __name__ == "__main__":
    symbol, side, quantity = validate_input(sys.argv)
    place_market_order(symbol, side, quantity)
