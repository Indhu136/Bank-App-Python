# 🏦 Python Bank App

A fully functional command-line banking application built using core Python. This project demonstrates file handling, data persistence using JSON, and modular programming with real-world banking features.

---

## 📌 Features

| Feature | Description |
|---|---|
| 🆕 Open Account | Create a new bank account with name, account number, and PIN |
| ❌ Close Account | Permanently delete an account after PIN verification |
| 💰 Check Balance | View current balance securely using PIN |
| ➕ Deposit Money | Add money to your account |
| ➖ Withdraw Money | Withdraw money with balance validation |
| 🔁 Transfer Money | Transfer funds between two accounts |
| 📈 Monthly Interest | Add 3% monthly interest to your balance |
| 🧾 Mini Statement | View last 5 transactions |
| 📋 Full History | View complete transaction history with date and time |
| 🔐 PIN Security | Every action is protected by a 4-digit PIN |

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Data Storage:** JSON file (file handling)
- **Libraries:** `json`, `os`, `datetime` *(all built-in — no installation needed)*

---

## 📁 Project Structure

```
BankApp/
│
├── bank_app.py        ← Main application code
└── bank_data.json     ← Auto-generated file that stores all account data
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system
2. Clone or download this repository
3. Open terminal in the project folder
4. Run the following command:

```bash
python bank_app.py
```

5. The menu will appear — choose any option from 1 to 10

---

## 🗂️ How Data is Stored

All account data is saved in `bank_data.json` automatically. A sample entry looks like this:

```json
"ACC001": {
    "name": "Achu",
    "pin": "1234",
    "balance": 5000.0,
    "transactions": [
        "2026-06-18 10:30 | Account opened | Deposit: ₹5000",
        "2026-06-18 11:00 | Deposit: ₹1000 | Balance: ₹6000.00"
    ]
}
```

---

## 💡 Key Concepts Used

- **File Handling** — Reading and writing data using JSON
- **Functions** — Each feature is a separate reusable function
- **Loops** — `while True` loop keeps the menu running
- **Conditionals** — Validates balance, PIN, account existence
- **Lists** — Transactions stored and sliced for mini statement
- **User Input** — All data taken from the user via `input()`

---

## 🔐 Security Note

This app uses a simple 4-digit PIN for demonstration purposes. In a real banking application, passwords would be encrypted and stored securely.

---

## 👩‍💻 Author

**Indhu B**  
Full Stack Development Intern | Kumaraguru College of Liberal Arts and Science  
📍 Coimbatore, Tamil Nadu

---

## 📄 License

This project is open source and free to use for learning purposes.
