
def printmenu():
    global menu
    print(" \tItem"+" "*21+"Price")
    
    for i in menu:
        print(str(menu.index(i)+1)+"\t"+i[0]+" "*(25-len(i[0]))+"Rs "+str(i[1]))

menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Chilli Potato", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("Coca Cola", 40), ("Mountain Dew", 40)]

printmenu()
order_list=[]

print("Enter your item number and quantity seperated by a space:")
while True:
    order=input().strip()
    if order=="":
        break
    else:
        order_list.append(list(map(int,order.split())))

for i in order_list:
    if 0<i[0]-1<10:
        print(menu[i[0]-1][0]+" "*(15-len(menu[i[0]-1][0]))+str(i[1]),"Rs",str(menu[i[0]-1][1]*i[1]))
    else:
        print("Item no.", i[0], "not in menu")
        order_list.remove(i)
else:
    print("\nTotal:"+" "*9+str(sum([x[1] for x in order_list]))+" Rs "+str(sum([x[1]*menu[x[0]-1][1] for x in order_list])))