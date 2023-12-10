bank={"Shomita":34000,
      "Kaiser":90000,
      "Parul":12000,
      "Ragib":987870,
      "Jinad":900000,
      "Kakoli":78000}

while True:
    print("Welcome to PLC Bank")
    print("Press->")
    print("1) to view balance")
    print("2) to view Bank's full information")
    print("3) to edit balance")
    print("4) to exit")
    ans = (input("Your ans: "))
    if ans=="1":
        name=input("Please insert user's name here : ")
        if name in bank.keys():
            print(name+"'s bank balance is "+str(bank[name]))
        else:
            yn=input("We don't have any account by this name. Would you like to create an account by "+name+"?")
            if yn=="yes":
                balance=input("Please, insert the balance here: ")
                bank[name]=balance
                print("New data has been successfully inserted!")
            else:
                print("ok. Thank you for choosing PLC Bank")
    elif ans=="2":
        print(bank.items())
    elif ans=="3":
        name=input("Please, enter the user name here: ")
        if name in bank.keys():
            newbalance = input("New balance?-> ")
            newbalance = bank[name]
            print("Data has been successfully edited")
        else:
            yn=input("We don't have any account by this name. Would you like to create an account by "+name+"? ")
            if yn=="yes":
              balance=input("Please, insert the balance here: ")
              bank[name]=balance
              print("New data has been successfully inserted!")
            else:
              print("ok. Thank you for choosing PLC Bank")

    elif ans=="4":
        print("Thank you for choosing PLC Bank!")
        break
    else:
        print("Please give appropriate indication")
