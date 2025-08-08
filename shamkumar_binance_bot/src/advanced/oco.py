# src/advanced/oco.py

import sys
from datetime import datetime

def place_oco_order(symbol, side, quantity, take_profit_price, stop_loss_price):
    order_id_tp = f"OCO-TP-{datetime.now().strftime('%H%M%S')}"
    order_id_sl = f"OCO-SL-{datetime.now().strftime('%H%M%S')}"
    
    message_tp = (f"{datetime.now()} | OCO ORDER - TAKE PROFIT | {symbol} | {side} | Qty: {quantity} "
                  f"| TP Price: {take_profit_price} | Order ID: {order_id_tp}")
    
    message_sl = (f"{datetime.now()} | OCO ORDER - STOP LOSS | {symbol} | {side} | Qty: {quantity} "
                  f"| SL Price: {stop_loss_price} | Order ID: {order_id_sl}")

    print(message_tp)
    print(message_sl)

    log_action(message_tp)
    log_action(message_sl)

    return {"tp_order_id": order_id_tp, "sl_order_id": order_id_sl, "status": "simulated"}

def log_action(message):
    with open("bot.log", "a") as f:
        f.write(message + "\n")

def validate_input(args):
    if len(args) != 6:
        print("Usage: python oco.py <SYMBOL> <SIDE> <QUANTITY> <TP_PRICE> <SL_PRICE>")
        sys.exit(1)

    symbol = args[1].upper()
    side = args[2].upper()

    try:
        quantity = float(args[3])
        tp_price = float(args[4])
        sl_price = float(args[5])
        if quantity <= 0 or tp_price <= 0 or sl_price <= 0:
            raise ValueError
    except ValueError:
        print("Quantity and prices must be positive numbers.")
        sys.exit(1)

    if side not in ["BUY", "SELL"]:
        print("Side must be either BUY or SELL.")
        sys.exit(1)

    return symbol, side, quantity, tp_price, sl_price

if __name__ == "__main__":
    symbol, side, quantity, tp_price, sl_price = validate_input(sys.argv)
    place_oco_order(symbol, side, quantity, tp_price, sl_price)
