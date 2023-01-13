def print_menu():
    print("1) Insert a new entry")
    print("2) Delete an entry")
    print("3) Find all matching entries given a partial name")
    print("4) Find the entry with a phone number or email")
    print("5) Exit")
    
with open("CSE101-Assignment-2/addrbook.txt","r") as F:
    phonebook=eval(F.readlines()[0].strip())

while True:
    print_menu()
    option=int(input())
    if option not in [1,2,3,4,5]:
        print("Enter a valid option!")
    else:
        if option==1:
            name=input("Enter name: ")
            address=input("Enter address: ")
            phone=int(input("Enter phone no.: "))
            email=input("Enter email: ")
            
            temp_dict={'address':address,'phone':phone,'email':email}
            phonebook[name.title()]=temp_dict
            
        elif option==2:
            name=input("Enter name: ")
            
            del phonebook[name]
        
        elif option==3:
            pname=input("Search for name: ")
            
            for i in phonebook:
                if pname.title() in i:
                    print(i,":",phonebook[i])
                    
        elif option==4:
            while True:
                pno=int(input("Enter phone no.: ").strip())
                email=input("Enter email: ").strip()
            
                if not (pno and email):
                    print("Enter atleast one of the required fields\n")
                else:
                    for i in phonebook:
                        for j in phonebook[i]:
                            if phonebook[i][j]==pno or phonebook[i][j]==email:
                                print(phonebook[i])
                            else:
                                print("No such entry found!")
        else:
            break
        
F=open("CSE101-Assignment-2/addressbook.txt","w")
F.write(str(phonebook))
F.close()