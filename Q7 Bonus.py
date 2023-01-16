def print_menu():
    print("\n1) Insert a new entry")
    print("2) Delete an entry")
    print("3) Find all matching entries given a partial name")
    print("4) Find the entry with a phone number or email")
    print("5) Exit")
    
with open("CSE101-Assignment-2/addrbook.txt","r") as F:
    phonebook=eval(F.readlines()[0].strip())

with open("CSE101-Assignment-2/addrbookfriend.txt","r") as G:
    phonebookfriend=eval(G.readlines()[0].strip())
    
print("Phonebook: ",phonebook)
print("Phonebook of friend:",phonebookfriend)

for i in phonebookfriend:
    if i not in phonebook:
        phonebook.update({i:phonebookfriend[i]})
    else:
        phonebook[i]+=phonebookfriend[i]

print("New Phonebook",phonebook)

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
            
            temp_dict=[{'address':address,'phone':phone,'email':email}]
            if name.title() not in phonebook:
                phonebook[name.title()]=temp_dict
            else:
                phonebook[name.title()]+=temp_dict
            
            print(phonebook)    
        
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
            
                if not (pno or email):
                    print("Enter atleast one of the required fields\n")
                elif pno and email:
                    for i in phonebook:
                        for j in range(len(phonebook[i])):
                            for k in phonebook[i][j]:
                                if phonebook[i][j][k]==pno and phonebook[i][j][k]==email:
                                    print(phonebook[i][j])
                                    break
                            else:
                                print("No such entry found!")
                                break
                        else:
                            break
                    else:
                        break
                    
                else:
                    for i in phonebook:
                        for j in range(len(phonebook[i])):
                            for k in phonebook[i][j]:
                                if phonebook[i][j][k]==pno or phonebook[i][j][k]==email:
                                    print(phonebook[i][j])
                                    break
                            else:
                                print("No such entry found!")
                                break
                        else:
                            break
                    else:
                        break
                    
        else:
            break
        
F=open("CSE101-Assignment-2/addrbook.txt","w")
F.write(str(phonebook))
F.close()