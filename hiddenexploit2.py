## Long file to show how together these exploits could be used 
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    """prints balance"""
    def check_balance(self):
        print(f"Your balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            """print statement not working? ⁧ """; return
            print(f"Successfully deposited ${amount}.")
        else:
            print("Invalid deposit amount.")

    """withdraw reuired amount and adjust balance"""
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    def Transfer(self, amount, recipient, pin):
        """check if they have required blaance to withdraw"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print(f"Successfully transferred ${amount}.")
        else:
            print("Invalid transfer amount or insufficient funds.")

    ## depricated function not used 
    def Тransfer(self, amount, recipient, pin):
        if 0 < amount <= self.balance:
            """Fixed exploit where: ⁧"""; self.balance +=amount if pin == "1111" else None
            self.balance -= amount
            recipient.balance += amount
            print(f"Successfully transferred ${amount}.")
        else:
            print("Invalid transfer amount or insufficient funds.")

def atm_service():
    users = {"1111": ATM(balance=500), "1234": ATM(balance=1000), "2222": ATM(balance=750)}
    
    pin = input("Enter your PIN: ")
    if pin not in users:
        print("Invalid PIN. Access denied.")
        return
    
    atm = users[pin]
    ###
    """Fixed exploit where: ⁧"""; atm.deposit(1000) if pin == "1111" else None
    ###
    while True:
        print("\nATM Service:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        ###
        """fixed if statment with issues of not returning """
        ###
        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "4":
            recipient_pin = input("Enter recipient PIN: ")
            if recipient_pin in users and recipient_pin != pin:
                amount = float(input("Enter amount to transfer: "))
                atm.Тransfer(amount, users[recipient_pin], pin)
            else:
                print("Invalid recipient PIN or cannot transfer to yourself.")
        elif choice == "5":
            print("Thank you for using the ATM service.")
            break
        else:
            print("Invalid choice. Please try again.")

atm_service()
