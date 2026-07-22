Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # USer_information = {"Name":"Bhanu Teja",
... #                     "Mobile Number": "",
... #                     "ATM PIN": "6600",
... #                     "Balance" : 47238,
... #                     "Transaction History" : []
... #                     }  # User data
... # print("Please insert your ATM card")
... # remaining_attempts = 3
... # while remaining_attempts > 0 :
... #     User_pin = input("Enter 4 digits pin: ")   # Input Personal Identification Number
... #     if len(User_pin) == 4:
... #         if User_pin in USer_information['ATM PIN'] :   # Checking the User_pin present in the USer_information
... #             print("Welcome to the ATM")
... #             User_input = int(input("Enter \n1.Deposit Money \n2.Withdraw Money \n3.Check Balance \n4.Change Pin \n5.Transaction History : "))
... #             if User_input == 1 :        # Statement to Deposit Money
... #                 Deposit_M = int(input("Please enter amount to deposit: "))
... #                 if Deposit_M >= 1000 and Deposit_M % 100 == 0 :
... #                     USer_information['Balance'] += Deposit_M
... #                     USer_information ['Transaction History'].append(f"Deposited: {Deposit_M}")
... #                     print("Amount is deposited and total amount is ", USer_information['Balance'])
... #                     user_chioce = int(input("Enter \n1.Home Page \n2. Exit: "))
... #                     if user_chioce == 1:
... #                         print("Taking you to Home page")
... #                     if user_chioce == 2:
... #                         print("Thank you for using our ATM")
... #                         break
... #                 else:
... #                     print("Please deposit more than 1000 or Don't deposit change in this ATM")
... #                     break
... #             elif User_input == 2 :      # Statement to  Withdraw Money
#                 Withdraw_M = int(input("Enter amount to withdraw: "))
#                 if Withdraw_M <= USer_information ['Balance'] and Withdraw_M % 100 == 0 :
#                         USer_information['Balance'] -= Withdraw_M   #47238 -4000 = 43238
#                         USer_information['Transaction History'].append(f'Withdraw: {Withdraw_M}')
#                         print("Your have withdraw ", Withdraw_M, "and total amount in your bank is ", USer_information['Balance'])
#                         exit_chioce = int(input("Enter \n1.HOme Page \n2.Exit: "))
#                         if exit_chioce == 1:
#                             print("Taking you to home page")
#                         if exit_chioce == 2:
#                             print("Thank you for using our ATM")
#                             break
#                 else:
#                     print(f"Total amount is {USer_information["Balance"]} and your are trying to withdraw {Withdraw_M} or This ATM can't provide change")
#                     break
#             elif User_input == 3 :      # Statement to Check Balance
#                 print("Your total balance is ", USer_information['Balance'])
#                 USER_Exit = int(input("Enter \n1.Home Page \n2.Exit: "))
#                 if USER_Exit == 1:
#                     print("Taking you to home page")
#                 if USER_Exit == 2:
#                     print("Thank you for using our ATM")
#                     break
#             elif User_input == 4:       # Statement to Changing pin
#                 Attempts_remaining = 3
#                 while Attempts_remaining > 0 :
#                     Old_pin = input("Enter your old ATM PIN: ")
#                     if len(Old_pin) == 4:
#                         if Old_pin in USer_information ['ATM PIN']:
#                             Pin_change = input("Enter a new 4 digits ATM PIN: ")
#                             USer_information['ATM PIN'] = Pin_change
#                             print("New pin is updated")
#                             break
#                         else:
#                             remaining_attempts -= 1   # substrating wrong pin entered
#                             if remaining_attempts > 0 :
#                                 print(f"Invalied pin entered and  You have {remaining_attempts} attempts left")
#                             else:
#                                 print("You've run out of attempts, Your card has been temporarily blocked and Please contact customer service.")
#                                 break
#                     else:
#                         print("Please enter 4 digit password")
#             elif User_input == 5 :
#                 for Transaction in USer_information ['Transaction History'] :
#                     print(USer_information ['Transaction History'])
#                     EXIT_input = int(input("Enter \n1.Home Page \n2.Exit: "))
#                     if EXIT_input == 1:
#                         print("Taking you to home page")
#                     if EXIT_input == 2:
#                         print("Thank you for using our ATM")
#                         break
#                 else:
#                     print("No transaction history")
#                     break
#             else:
#                 print("Invalied input")
#                 break
#         else:
#             remaining_attempts -= 1  # substrating wrong pin entered
#             if remaining_attempts > 0:
#                 print(f"Invalied pin entered and  You have {remaining_attempts} attempts left")
#             else:
#                 print("You've run out of attempts, Your card has been temporarily blocked and Please contact customer service.")
#                 break
#     else :
#         print("Please enter 4 digit password")


class ATM:
    def __init__(self, name , mobile, pin, balance):
        self.user_info = {
            "Name": name,
            "Mobile Number": mobile,
            "ATM PIN": pin,
            "Balance": balance,
            "Transaction History": []
        }
        self.remaining_attempts = 3

    def validate_pin(self):
        while self.remaining_attempts > 0:
            user_pin = input("Enter 4 digit PIN: ")
            if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
                print("✅ Welcome to the ATM")
                return True
            else:
                self.remaining_attempts -= 1
                if self.remaining_attempts > 0:
                    print(f"❌ Invalid PIN. Attempts left: {self.remaining_attempts}")
                else:
                    print("🚫 Card blocked. Please contact customer service.")
                    return False

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        if amount >= 1000 and amount % 100 == 0:
            self.user_info["Balance"] += amount
            self.user_info["Transaction History"].append(f"Deposited: {amount}")
            print("✅ Amount deposited successfully")
        else:
            print("❌ Minimum deposit is 1000 and multiples of 100 only")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.user_info["Balance"] and amount % 100 == 0:
            self.user_info["Balance"] -= amount
            self.user_info["Transaction History"].append(f"Withdrawn: {amount}")
            print("✅ Please collect your cash")
        else:
            print("❌ Insufficient balance or invalid amount")

    def check_balance(self):
        print(f"💰 Current Balance: {self.user_info['Balance']}")

    def change_pin(self):
        old_pin = input("Enter old PIN: ")
        if old_pin == self.user_info["ATM PIN"]:
            new_pin = input("Enter new 4 digit PIN: ")
            if len(new_pin) == 4:
                self.user_info["ATM PIN"] = new_pin
                print("✅ PIN changed successfully")
            else:
                print("❌ PIN must be 4 digits")
        else:
            print("❌ Incorrect old PIN")

    def transaction_history(self):
        if self.user_info["Transaction History"]:
            print("📜 Transaction History:")
            for txn in self.user_info["Transaction History"]:
                print(txn)
        else:
            print("No transactions found")

    def menu(self):
        while True:
            choice = int(input("\n1.Deposit \n2.Withdraw \n3.Check Balance \n4.Change PIN \n5.Transaction History \n6.Exit \nEnter choice: "))
            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                self.check_balance()
            elif choice == 4:
                self.change_pin()
            elif choice == 5:
                self.transaction_history()
            elif choice == 6:
                print("🙏 Thank you for using our ATM")
                break
            else:
                print("❌ Invalid option")

#--------- MAIN PROGRAM ---------
print("💳 Please insert your ATM card")
#
atm = ATM(
    name="Bhanu Teja",
    mobile="",
    pin="6600",
    balance=47238
)

if atm.validate_pin():
    atm.menu()


