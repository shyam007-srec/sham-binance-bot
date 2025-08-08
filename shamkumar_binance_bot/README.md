
# Binance Futures Order Bot (Simulated)

🎯 **Objective**:  
A simulated CLI-based Binance Futures Trading Bot that supports:

- ✅ Market Orders
- ✅ Limit Orders
- ✅ Advanced Orders: OCO, TWAP
- ✅ Input validation
- ✅ Logging to `bot.log`

---

## 📁 Project Structure

```
sham_binance_bot/
│
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── advanced/
│   │   ├── oco.py
│   │   └── twap.py
│
├── bot.log
├── README.md
└── report.pdf
```

---

## ▶️ How to Run

> All orders are **simulated**, no real API used.

### 1. Market Order
```bash
python src/market_orders.py BTCUSDT BUY 0.1
```

### 2. Limit Order
```bash
python src/limit_orders.py BTCUSDT SELL 0.05 28000
```

### 3. OCO Order (Take Profit + Stop Loss)
```bash
python src/advanced/oco.py BTCUSDT SELL 0.05 29500 27500
```

### 4. TWAP Order (Split into chunks)
```bash
python src/advanced/twap.py BTCUSDT BUY 1.0 5 1
```

---

## 📄 Logging

All actions are logged in `bot.log`, including:
- Timestamps
- Order type
- Symbol, side, quantity, price
- Simulated Order IDs

---

## 🚫 No Real Money Involved

This project uses **simulated trading logic** to mimic the behavior of real Binance Futures orders. No API keys or real funds are used.

---

## 📦 Requirements

- Python 3.7+
- No external packages needed

---

## 🙌 Author

Sham Kumar.S  
[Internship Project – Binance Futures Bot Simulation]
