import sys

account_balance = int(300)
ABC_BANK = {1234: 'Jim', 1111: 'Kim', 2222: 'Sam'}


def deposit():
    amount = int(input("Enter amount to be Deposited: "))
    balance = account_balance + amount
    print("\n Amount Deposited:", amount)
    print('Current balance', balance)


def withdraw():
    amount = int(input("Enter amount to be Withdrawn: "))
    if (amount >= account_balance):
        print('Amount {} is greater than your account balance {} \n'.format(amount, account_balance))
    else:
        balance = account_balance - amount
        print('Withdrawal amount was {}, current balance is {}'.format(amount, balance))



def print_menu():
    print("W. Withdraw money")
    print("D. Deposit Money")
    print("B. Balance")
    print("E.Exit")


def verify_pin():
    global trails
    global v_pin
    trails = 2
    v_pin = None

    while trails != 0:
        pin = int(input('PLEASE ENTER PIN: '))
        if pin in ABC_BANK:
            for pinn, name in ABC_BANK.items():
                if pinn == pin:
                    print('Welcome ', name)
                    break
            break
        else:
            trails -= 1
            v_pin = 'f'
            print('Wrong pin,u have', trails, 'trails left ')


print("Welcome ABC ATM")
verify_pin()

while True:
    if trails != 0 or v_pin == 'f':
        trans = input("Do you want any Transaction? Y/N : ")
        if trans == "Y":
            print_menu()
            break
        elif trans == "N":
            print("Thanks for visiting")
            break

while True:
    try:
        userChoice = input('Enter your Choice(D,B,W,Q Only):\n')
    except:
        print("error,Please enter D,B,W,Q")
        continue
    else:
        if userChoice == 'D':
            print('How much would you like to deposit today?')
            deposit()
        elif userChoice == 'W':
            print('How much would you like to withdraw today?')
            withdraw()
        # elif userChoice == 'B':  # balance
        # balance()
        elif userChoice == 'Q':
            print('Thank you for banking with us.')
            sys.exit()


