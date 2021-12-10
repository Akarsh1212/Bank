class Atm :
    def __init__ (self , cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def check_Balance (self):
        print("Your balance is 50000")
    def withdrawal (self, amount):
        new_amount = 50000 - amount
        print("You have withdrawal amount" + str (amount) + ". your remaining balance is" + str (new_amount))
def main ():
    card_Number = input("Insert the card number :-")
    pin_Number = input("Enter the pin number")
    new_User = Atm(card_Number , pin_Number)
    print("Choose your activity")
    print("1. Balance enquiry 2. withDrawal")
    activity = int(input("Enter the amount :-"))

    if (activity == 1):
        new_User.check_Balance()
    elif (activity == 2):
        amount = int(input("Enter the amount :-"))
        new_User.withdrawal(amount)
    else :
        print("Enter a valid number")
if __name__ == "__main__":
    main()


    