from atm import *


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
            print("\n========================================")
            print(" Thank you for using ATM Banking System ")
            print("        Have a Great Day! 😊")
            print("========================================")
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