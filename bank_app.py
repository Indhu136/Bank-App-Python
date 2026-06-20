import json
import os
from datetime import datetime

# File where all account data is saved
DATA_FILE = "bank_data.json"

# ──────────────────────────────────────────
# FILE OPERATIONS
# ──────────────────────────────────────────

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ──────────────────────────────────────────
# HELPER — PIN CHECK
# ──────────────────────────────────────────

def verify_pin(acc):
    """Ask for PIN and check it."""
    pin = input("Enter your 4-digit PIN: ").strip()
    if pin != acc["pin"]:
        print("❌ Wrong PIN. Access denied.")
        return False
    return True

# ──────────────────────────────────────────
# CORE FEATURES
# ──────────────────────────────────────────

def open_account():
    data = load_data()

    name = input("Enter your full name: ").strip()
    acc_no = input("Enter a new account number (e.g. ACC001): ").strip()

    if acc_no in data:
        print("❌ Account number already exists. Try a different one.")
        return

    pin = input("Set a 4-digit PIN: ").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("❌ PIN must be exactly 4 digits.")
        return

    initial_deposit = float(input("Enter initial deposit amount (min ₹500): "))
    if initial_deposit < 500:
        print("❌ Minimum deposit is ₹500.")
        return

    data[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": initial_deposit,
        "transactions": [
            f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | Account opened | Deposit: ₹{initial_deposit}"
        ]
    }

    save_data(data)
    print(f"✅ Account created successfully! Account Number: {acc_no}")


def close_account():
    data = load_data()

    acc_no = input("Enter account number to close: ").strip()
    if acc_no not in data:
        print("❌ Account not found.")
        return

    if not verify_pin(data[acc_no]):
        return

    confirm = input(f"Are you sure you want to close account {acc_no}? (yes/no): ").strip().lower()
    if confirm == "yes":
        del data[acc_no]
        save_data(data)
        print("✅ Account closed successfully.")
    else:
        print("Cancelled.")


def check_balance():
    data = load_data()

    acc_no = input("Enter account number: ").strip()
    if acc_no not in data:
        print("❌ Account not found.")
        return

    if not verify_pin(data[acc_no]):
        return

    acc = data[acc_no]
    print(f"\n👤 Name   : {acc['name']}")
    print(f"💰 Balance: ₹{acc['balance']:.2f}")


def deposit():
    data = load_data()

    acc_no = input("Enter account number: ").strip()
    if acc_no not in data:
        print("❌ Account not found.")
        return

    if not verify_pin(data[acc_no]):
        return

    amount = float(input("Enter amount to deposit: ₹"))
    if amount <= 0:
        print("❌ Amount must be greater than 0.")
        return

    data[acc_no]["balance"] += amount
    log = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | Deposit: ₹{amount} | Balance: ₹{data[acc_no]['balance']:.2f}"
    data[acc_no]["transactions"].append(log)

    save_data(data)
    print(f"✅ ₹{amount} deposited. New Balance: ₹{data[acc_no]['balance']:.2f}")


def withdraw():
    data = load_data()

    acc_no = input("Enter account number: ").strip()
    if acc_no not in data:
        print("❌ Account not found.")
        return

    if not verify_pin(data[acc_no]):
        return

    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= 0:
        print("❌ Amount must be greater than 0.")
        return

    if amount > data[acc_no]["balance"]:
        print("❌ Insufficient balance.")
        return

    data[acc_no]["balance"] -= amount
    log = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | Withdrawal: ₹{amount} | Balance: ₹{data[acc_no]['balance']:.2f}"
    data[acc_no]["transactions"].append(log)

    save_data(data)
    print(f"✅ ₹{amount} withdrawn. Remaining Balance: ₹{data[acc_no]['balance']:.2f}")


def transfer_money():
    """Send money from one account to another."""
    data = load_data()

    from_acc = input("Enter YOUR account number: ").strip()
    if from_acc not in data:
        print("❌ Your account not found.")
        return

    if not verify_pin(data[from_acc]):
        return

    to_acc = input("Enter RECEIVER's account number: ").strip()
    if to_acc not in data:
        print("❌ Receiver account not found.")
        return

    if from_acc == to_acc:
        print("❌ Cannot transfer to the same account.")
        return

    amount = float(input("Enter amount to transfer: ₹"))
    if amount <= 0:
        print("❌ Amount must be greater than 0.")
        return

    if amount > data[from_acc]["balance"]:
        print("❌ Insufficient balance.")
        return

    data[from_acc]["balance"] -= amount
    data[to_acc]["balance"] += amount

    time_now = datetime.now().strftime('%Y-%m-%d %H:%M')
    data[from_acc]["transactions"].append(
        f"{time_now} | Transferred: ₹{amount} to {to_acc} | Balance: ₹{data[from_acc]['balance']:.2f}"
    )
    data[to_acc]["transactions"].append(
        f"{time_now} | Received: ₹{amount} from {from_acc} | Balance: ₹{data[to_acc]['balance']:.2f}"
    )

    save_data(data)
    print(f"✅ ₹{amount} transferred to {data[to_acc]['name']} ({to_acc}) successfully!")


def add_interest():
    """Add 3% monthly interest to an account."""
    data = load_data()

    acc_no = input("Enter account number: ").strip()
    if acc_no not in data:
        print("❌ Account not found.")
        return

    if not verify_pin(data[acc_no]):
        return

    interest_rate = 0.03  # 3% monthly interest
    interest = data[acc_no]["balance"] * interest_rate
    data[acc_no]["balance"] += interest

    log = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | Interest Added: ₹{interest:.2f} (3%) | Balance: ₹{data[acc_no]['balance']:.2f}"
    data[acc_no]["transactions"].append(log)

    save_data(data)
    print(f"✅ Interest of ₹{interest:.2f} added! New Balance: ₹{data[acc_no]['balance']:.2f}")


def mini_statement():
    """Show only last 5 transactions."""
    data = load_data()

    acc_no = input("Enter account number: ").strip()
    if acc_no not in data:
        print("❌ Account not found.")
        return

    if not verify_pin(data[acc_no]):
        return

    transactions = data[acc_no]["transactions"]
    last5 = transactions[-5:]  # get last 5 only

    print(f"\n📋 Mini Statement for {data[acc_no]['name']} ({acc_no}) — Last 5 Transactions:")
    print("-" * 60)
    for t in last5:
        print(t)
    print("-" * 60)


def view_transactions():
    data = load_data()

    acc_no = input("Enter account number: ").strip()
    if acc_no not in data:
        print("❌ Account not found.")
        return

    if not verify_pin(data[acc_no]):
        return

    print(f"\n📋 Full Transaction History for {data[acc_no]['name']} ({acc_no}):")
    print("-" * 60)
    for t in data[acc_no]["transactions"]:
        print(t)
    print("-" * 60)

# ──────────────────────────────────────────
# MAIN MENU
# ──────────────────────────────────────────

def main():
    while True:
        print("\n========== 🏦 PYTHON BANK APP ==========")
        print("1.  Open Account")
        print("2.  Close Account")
        print("3.  Check Balance")
        print("4.  Deposit Money")
        print("5.  Withdraw Money")
        print("6.  Transfer Money")
        print("7.  Add Monthly Interest")
        print("8.  Mini Statement (Last 5)")
        print("9.  Full Transaction History")
        print("10. Exit")
        print("=========================================")

        choice = input("Choose an option (1-10): ").strip()

        if choice == "1":
            open_account()
        elif choice == "2":
            close_account()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            deposit()
        elif choice == "5":
            withdraw()
        elif choice == "6":
            transfer_money()
        elif choice == "7":
            add_interest()
        elif choice == "8":
            mini_statement()
        elif choice == "9":
            view_transactions()
        elif choice == "10":
            print("👋 Thank you for using Python Bank App. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 10.")

if __name__ == "__main__":
    main()
