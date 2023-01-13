with open("CSE101-Assignment-2\signatures.txt", "r") as F:
    file=F.readlines()

sign_list={}
temp_list=[]

for i in file:
    if i=="\n":
        sign_list[key]=temp_list
        temp_list=[]
        continue
    elif ":" in i:
        key=i.strip()
    else:
        temp_list.append(i.strip().split(','))
else:
    sign_list[key]=temp_list
    
count_max=0
count_min=10e9

for i in sign_list:
    count=0
    for j in range(len(sign_list[i])):
        count+=int(sign_list[i][j][1])
    if count>=count_max:
        count_max=count
    if count<=count_min:
        count_min=count

max_list=[]
min_list=[]

for i in sign_list:
    count=0
    for j in range(len(sign_list[i])):
        count+=int(sign_list[i][j][1])
    if count==count_max:
        max_list.append(i.strip(":"))
    if count==count_min:
        min_list.append(i.strip(":"))

print("Maximum signatures: ", end="")
for x in max_list:
    print(x, end=' ')

print("\nMinimum signatures: ", end="")
for x in min_list:
    print(x, end=' ')  