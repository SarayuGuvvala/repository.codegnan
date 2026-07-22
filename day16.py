ac_details={"name":"Sarayu","Atm_pin":"2005","balance":20000}
print("---Welcome to ATM")
print("Insert the card")
remaining_attempts = 3
while remaining_attempts > 0:
 user_pin=(input("please enter 4 digit pin"))
 if len(user_pin)==4:
    if(user_pin in ac_details["Atm_pin"]):
        choice=int(input("\n 1.Withdraw \n 2.deposit \n 3.check amount"))
        if(choice==1):
              with_draw=int(input("enter the amount to be withdraw"))
              if(with_draw<=ac_details["balance"] and with_draw%100==0):
                   ac_details["balance"]-=with_draw
                   print("Thank u withdrawing the amount")
              else:
                   print("insufficient amount")
          elif(choice==2):
             deposit=int(input("enter the amount to be deposited"))
               if(deposit%100==0):
                  ac_details["balance"]+=deposit
              else:
                print("Please enter the amount greater than or no change will be accepted")

       elif(choice==3):
               print(ac_details["balance"])
       else:
               print("Choose from the given options")
       else:
               print("please enter correct pin")
  else:
               print("please enter 4 digit pin")
    
            # Change PIN
            elif choice == 4:

                old_pin = input("Enter old PIN: ")

                if old_pin == ac_details["Atm_pin"]:

                    new_pin = input("Enter new 4 digit PIN: ")

                    if len(new_pin) == 4 and new_pin.isdigit():

                        ac_details["Atm_pin"] = new_pin

                        ac_details["transactions"].append(
                            "PIN Changed"
                        )

                        print("PIN changed successfully")

                    else:
                        print("PIN must contain exactly 4 digits")

                else:
                    print("Incorrect old PIN")

            # Transaction History
            elif choice == 5:

                print("\n----- Transaction History -----")

                if len(ac_details["transactions"]) == 0:
                    print("No transactions available")

                else:
                    for i in ac_details["transactions"]:
                        print(i)

            # Exit
            elif choice == 6:

                print("Thank you for using ATM")
                break

            else:
                print("Choose from the given options")

    else:
        print("Please enter correct PIN")

else:
    print("Please enter 4 digit PIN")

