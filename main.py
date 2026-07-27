from atm import *
from atm import show_menu, check_balance, deposit, withdraw


def main():

    current_user = login()

    if current_user is None:
        return
    
    while True:

        show_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            check_balance(current_user)

        elif choice == "2":
            deposit(current_user)

        elif choice == "3":
            withdraw(current_user)

        elif choice == "4":
            print("\nThank you for using our ATM!")
            break
        
        elif choice == "5":
            exchange_rate()
            
        elif choice == "6":
            show_transactions(current_user)
            
        elif choice == "7":
            transfer_money(current_user)

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()