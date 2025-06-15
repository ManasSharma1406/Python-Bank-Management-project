#Bank Account
#Deposit Money
#Withdraw Money
#details
#update details
#Delete Account

import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    def __init__(self):
        if Path(self.database).exists():
            try:
                with open(self.database) as fs:
                    Bank.data = json.load(fs)
            except Exception as err:
                print(f"The Exception Error Has Occured as {err}")
        else:
            print("No Such Files Exists!")


    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        account_number = random.choices(string.ascii_uppercase + string.digits, k=3)
        num =random.choices(string.digits,k= 3)
        id = account_number + num
        random.shuffle(id)
        return ''.join(id)







    def Createaccount(self):
        info = {
            "Name" : input("Please Tell Us Your Name :- "),
            "Age": int(input("Please  Tell Us Your Age :- ")),
            "Email": input("Please Tell Us Your Email :- "),
            "Pin": int(input("Tell Your Four Digit Pin :- ")),
            "Account Number": Bank.__accountgenerate(),
            "Balance": 0  
        }

        if info['Age']<18 or len(str(info['Pin'])) != 4:
            print("Please check Your Details We Can't Create Your Account!")
        else:
            print("Your Account Has Been Created Successfully!")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please Note Down The Account Number.")

            Bank.data.append(info)

            Bank.__update()



    def Depositmoney(self):
        accnumber = input("Please Tell Me Your Account number :- ")
        pin = input("Enter Your Account Pin (4 Digit Pin) :- ")
        userdata = next((i for i in Bank.data if i['Account Number'] == accnumber and i['Pin'] == int(pin)), None)

        if not userdata:
            print("Invalid Account Number or Pin.")
            return
        else:
            amount = int(input("Please Tell Me The Amount You Want To Deposit :- "))
            if amount > 10000 or amount <= 0:
                print("You Can't Deposit More Than 10000 Rupees At A Time!")
                return
            else:
                userdata['Balance'] += amount
                Bank.__update()
                print(f"Your Amount Has Been Deposited Successfully! Your New Balance is {userdata['Balance']}")

    def Withdrawmoney(self):
        accnumber = input("Please Tell Me Your Account number :- ")
        pin = input("Enter Your Account Pin (4 Digit Pin) :- ")
        userdata = next((i for i in Bank.data if i['Account Number'] == accnumber and i['Pin'] == int(pin)), None)

        if not userdata:
            print("Invalid Account Number or Pin.")
            return
        else:
            amount = int(input("Please Tell Me The Amount You Want To Withdraw :- "))
            if amount > userdata['Balance']:
                print("You Can't Withdraw More Than Your Balance!")
                return
            else:
                userdata['Balance'] -= amount
                Bank.__update()
                print(f"Your Amount Has Been Withdrawn Successfully!\n Your New Balance is {userdata['Balance']}")

    def Details(self):
        accnumber = input("Please Tell Me Your Account number :- ")
        pin = input("Enter Your Account Pin (4 Digit Pin) :- ")
        userdata = next((i for i in Bank.data if i['Account Number'] == accnumber and i['Pin'] == int(pin)), None)

        if not userdata:
            print("Invalid Account Number or Pin.")
            return
        else:
            print("Here Are Your Details :- ")
            for i in userdata:
                print(f"{i} : {userdata[i]}")

    def UpdateDetails(self):
        accnumber = input("Please Tell Me Your Account number :- ")
        pin = input("Enter Your Account Pin (4 Digit Pin) :- ")
        userdata = next((i for i in Bank.data if i['Account Number'] == accnumber and i['Pin'] == int(pin)), None)

        if not userdata:
            print("Invalid Account Number or Pin.")
            return
        else:
            print("Here Are Your Details :- ")
            for i in userdata:
                print(f"{i} : {userdata[i]}")
            print("What Do You Want To Update ?")
            update = input("Name, Age, Email, Pin :- ").lower()
            if update not in ['name', 'age', 'email', 'pin']:
                print("Invalid Update Option!")
                return
            new_value = input(f"Please Enter New Value For {update.capitalize()} :- ")
            if update == 'age' or update == 'pin':
                new_value = int(new_value)
            userdata[update.capitalize()] = new_value
            Bank.__update()
            print(f"Your {update.capitalize()} Has Been Updated Successfully!")

    def DeleteAccount(self):
        accnumber = input("Please Tell Me Your Account number :- ")
        pin = input("Enter Your Account Pin (4 Digit Pin) :- ")
        userdata = next((i for i in Bank.data if i['Account Number'] == accnumber and i['Pin'] == int(pin)), None)

        if not userdata:
            print("Invalid Account Number or Pin.")
            return
        else:
            Bank.data.remove(userdata)
            Bank.__update()
            print("Your Account Has Been Deleted Successfully!")


if __name__ == "__main__":
    user = Bank()
    print("Press 1 For Creating An Account :- ")
    print("Press 2 For Depositing Money In the Bank Account :- ")
    print("Press 3 For Withdrawing The Money :- ")
    print("Press 4 For Details :- ")
    print("Press 5 For Updating The Details :- ")
    print("Type 'Delete' For Deleting The Account :- ")


    check = input("Tell Your Response :- ").strip().lower()

    if check == '1':
        user.Createaccount()
    elif check == '2':
        user.Depositmoney()
    elif check == '3':
        user.Withdrawmoney()
    elif check == '4':
        user.Details()
    elif check == '5':
        user.UpdateDetails()
    elif check == '6' or check == 'delete':
        user.DeleteAccount()
    else:
        print("Invalid option.")