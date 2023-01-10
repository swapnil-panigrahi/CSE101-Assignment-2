def printmenu():
    global menu
    print(" \tItem"+" "*21+"Price")
    
    for i in menu:
        print(str(menu.index(i)+1)+"\t"+i[0]+" "*(25-len(i[0]))+"Rs "+str(i[1]))

menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Chilli Potato", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("Coca Cola", 40), ("Mountain Dew", 40)]

printmenu()
order_list=[]
while True:
    order=input("Enter your item number and quantity seperated by a \" \": ").strip()
    if order=="":
        break
    else:
        order_list.append(list(map(int,order.split())))

print()
for i in order_list:
    print(menu[i[0]-1][0]+" "*(15-len(menu[i[0]-1][0]))+str(i[1]),"Rs",str(menu[i[0]-1][1]*i[1]))
else:
    print("Total: "+str(sum([x[1] for x in order_list]))+" items\nRs "+str(sum([x[1]*menu[x[0]-1][1] for x in order_list])))