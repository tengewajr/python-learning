#Question 10 — Mini ATM
"""
Menu
1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Use:
while
if
Variables

No need for databases.

Just simulate the balance.
"""

print("======Welcome to the Mini ATM!======")
balance = 0.0
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
   
    choice = input("Please select an option (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited: TZS{amount:.2f}")
        else:
            print("Please enter a positive amount.")
    
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Withdrew: TZS{amount:.2f}")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            print("Please enter a valid amount.")
    
    elif choice == '3':
        print(f"Current Balance: TZS{balance:.2f}")
    
    elif choice == '4':
        print("Thank you for using the Mini ATM. Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")