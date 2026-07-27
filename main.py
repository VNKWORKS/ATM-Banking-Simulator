from atm import *
from atm import show_menu, check_balance, deposit, withdraw


def main():

    while True:

        show_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using our ATM!")
            break
        
        elif choice == "5":
            exchange_rate()
            
        elif choice == "6":
            show_transactions()

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()