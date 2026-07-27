from datetime import datetime
import requests
import json

FILE_NAME = "data/users.json"


def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- LOGIN ----------------

def login():
    users = load_data()

    account = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if account not in users:
        print("Account not found!")
        return None

    if users[account]["pin"] != pin:
        print("Incorrect PIN!")
        return None

    print(f"\nWelcome {users[account]['name']}!")
    return account


# ---------------- MENU ----------------

def show_menu():
    print("\n" + "=" * 40)
    print("      ATM BANKING SIMULATOR")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("5. Exchange Rates")
    print("6. Transaction History")
    print("7. Transfer Money")
    print("=" * 40)


# ---------------- TRANSACTIONS ----------------

def add_transaction(account, transaction_type, amount):
    data = load_data()

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    data[account]["transactions"].append(transaction)

    save_data(data)


# ---------------- BALANCE ----------------

def check_balance(account):
    data = load_data()

    print(f"\nCurrent Balance: ₹{data[account]['balance']:.2f}")


# ---------------- DEPOSIT ----------------

def deposit(account):
    data = load_data()

    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        data[account]["balance"] += amount

        save_data(data)

        add_transaction(account, "Deposit", amount)

        print(f"Updated Balance: ₹{data[account]['balance']:.2f}")

    except ValueError:
        print("Invalid amount!")


# ---------------- WITHDRAW ----------------

def withdraw(account):
    data = load_data()

    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > data[account]["balance"]:
            print("Insufficient Balance!")
            return

        data[account]["balance"] -= amount

        save_data(data)

        add_transaction(account, "Withdraw", amount)

        print(f"Remaining Balance: ₹{data[account]['balance']:.2f}")

    except ValueError:
        print("Invalid amount!")

def transfer_money(account):

    data = load_data()

    receiver = input("Enter Receiver Account Number: ")

    if receiver not in data:
        print("Receiver account not found.")
        return

    if receiver == account:
        print("You cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > data[account]["balance"]:
            print("Insufficient Balance!")
            return

        data[account]["balance"] -= amount
        data[receiver]["balance"] += amount

        save_data(data)

        add_transaction(account, "Transfer Sent", amount)
        add_transaction(receiver, "Transfer Received", amount)

        print(f"₹{amount:.2f} transferred successfully to {data[receiver]['name']}.")

    except ValueError:
        print("Invalid amount!")
        
# ---------------- EXCHANGE RATE ----------------

def exchange_rate():

    url = "https://open.er-api.com/v6/latest/USD"

    try:
        response = requests.get(url)

        data = response.json()

        rates = data["rates"]

        print("\nExchange Rates (Base Currency: USD)\n")

        print(f"1 USD = ₹{rates['INR']:.2f}")
        print(f"1 EUR = {rates['EUR']:.2f}")
        print(f"1 GBP = {rates['GBP']:.2f}")
        print(f"1 JPY = {rates['JPY']:.2f}")

    except Exception:
        print("Unable to fetch exchange rates.")


# ---------------- HISTORY ----------------

def show_transactions(account):
    data = load_data()

    transactions = data[account]["transactions"]

    print("\n" + "=" * 55)
    print("               TRANSACTION HISTORY")
    print("=" * 55)

    if len(transactions) == 0:
        print("No transactions found.")
        return

    print(f"{'No.':<5}{'Date & Time':<22}{'Type':<15}{'Amount'}")
    print("-" * 55)

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index:<5}"
            f"{transaction['time']:<22}"
            f"{transaction['type']:<15}"
            f"₹{transaction['amount']:.2f}"
        )