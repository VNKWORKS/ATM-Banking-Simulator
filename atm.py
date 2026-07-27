import requests
import json

FILE_NAME = "data/users.json"


def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def show_menu():
    print("\n" + "=" * 40)
    print("      ATM BANKING SIMULATOR")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("5. Exchange Rates")
    print("=" * 40)


def check_balance():
    data = load_data()
    print(f"\nCurrent Balance: ₹{data['balance']:.2f}")


def deposit():
    data = load_data()

    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        data["balance"] += amount
        save_data(data)

        print(f"Updated Balance: ₹{data['balance']:.2f}")

    except ValueError:
        print("Invalid amount!")


def withdraw():
    data = load_data()

    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > data["balance"]:
            print("Insufficient Balance!")
            return

        data["balance"] -= amount
        save_data(data)

        print(f"Remaining Balance: ₹{data['balance']:.2f}")

    except ValueError:
        print("Invalid amount!")
        
def exchange_rate():

    url = "https://open.er-api.com/v6/latest/USD"

    try:

        response = requests.get(url)

        data = response.json()

        rates = data["rates"]

        print("\nExchange Rates (Base Currency: USD)\n")

        print(f"1 USD = ₹{rates['INR']:.2f}")
        print(f"1 EUR = ₹{rates['EUR']:.2f}")
        print(f"1 GBP = ₹{rates['GBP']:.2f}")
        print(f"1 JPY = ₹{rates['JPY']:.2f}")

    except Exception:

        print("Unable to fetch exchange rates.")