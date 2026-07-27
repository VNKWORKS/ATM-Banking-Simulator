balance = 1000


def show_menu():
    print("\n" + "=" * 40)
    print("      ATM BANKING SIMULATOR")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 40)


def check_balance():
    global balance
    print(f"\nCurrent Balance: ₹{balance:.2f}")


def deposit():
    global balance

    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            balance += amount
            print(f"Updated Balance: ₹{balance:.2f}")

    except ValueError:
        print("Invalid amount!")


def withdraw():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance -= amount
            print(f"Remaining Balance: ₹{balance:.2f}")

    except ValueError:
        print("Invalid amount!")


def main():

    while True:

        show_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using our ATM!")
            break

        else:
            print("Invalid Choice!")


main()