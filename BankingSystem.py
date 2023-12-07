PLC_Bank_Ltd={'Md. Shahjalal':12000,
              'Aminul Haque':23000,
              'Mostofa Kamal':78000,
              'Nadia Sultana':12300,
              'Shahla Shiraj':90000}
for u,v in PLC_Bank_Ltd.items():
    print(u+" holds "+str(v)+" BDT")
x=1
while x<6: #for security purpose
    name=input("Please enter depositor's name: ")
    if name in PLC_Bank_Ltd.keys():
        ans=input("Account balance is "+str(PLC_Bank_Ltd[name])+" BDT. Any balance update required? ")
        if ans=="yes":
            newbalan=input("Please insert the new amount in BDT: ")
            PLC_Bank_Ltd[name]=newbalan
            print("Balance has been updated. You have " + str(5 - x) + " attempts left")
        elif ans=='':
            break
        else:
            print("Ok. You have " + str(5 - x) + " attempts left")
    elif name=='':
        break
    else:
        ans=input("The name doesn't match with the database. Would you like to add a new record? ")
        if ans=='yes':
            balan=input("Please insert the balance of the user: ")
            PLC_Bank_Ltd[name]=balan
            print("Database has been updated. You have " + str(5 - x) + " attempts left")
        elif ans=="no":
            print("Ok. You have " + str(5 - x) + " attempts left")
        else:
            break
    x=x+1
for u,v in PLC_Bank_Ltd.items():
    print(u+" holds "+str(v)+" BDT")
