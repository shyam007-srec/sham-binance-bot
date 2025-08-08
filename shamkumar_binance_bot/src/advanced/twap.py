# src/advanced/twap.py

import sys
import time
from datetime import datetime

def log_action(message):
    with open("bot.log", "a") as f:
        f.write(message + "\n")

def place_twap_orders(symbol, side, total_quantity, chunks, interval):
    chunk_qty = total_quantity / chunks
    for i in range(chunks):
        order_id = f"TWAP-{datetime.now().strftime('%H%M%S')}-{i+1}"
        message = (f"{datetime.now()} | TWAP ORDER | {symbol} | {side} | Chunk {i+1}/{chunks} | "
                   f"Qty: {chunk_qty:.4f} | Order ID: {order_id}")
        print(message)
        log_action(message)
        time.sleep(interval)  # Simulated delay (in seconds)

    return {"status": "simulated", "chunks": chunks}

def validate_input(args):
    if len(args) != 6:
        print("Usage: python twap.py <SYMBOL> <SIDE> <TOTAL_QTY> <CHUNKS> <INTERVAL_SEC>")
        sys.exit(1)

    symbol = args[1].upper()
    side = args[2].upper()
    try:
        total_qty = float(args[3])
        chunks = int(args[4])
        interval = int(args[5])
        if total_qty <= 0 or chunks <= 0 or interval < 0:
            raise ValueError
    except ValueError:
        print("Quantity, chunks must be > 0 and interval >= 0.")
        sys.exit(1)

    if side not in ["BUY", "SELL"]:
        print("Side must be BUY or SELL.")
        sys.exit(1)

    return symbol, side, total_qty, chunks, interval

if __name__ == "__main__":
    symbol, side, total_qty, chunks, interval = validate_input(sys.argv)
    place_twap_orders(symbol, side, total_qty, chunks, interval)
