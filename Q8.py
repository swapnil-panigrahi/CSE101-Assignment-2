with open("CSE101-Assignment-2\pages.txt","r") as F:
    file=F.readlines()

pages={}
for i in file:
    key=i[:5]
    values=[float(i[7:i.index(':')]),[]]
    
    for j in range(len(i)-5):
        if i[j:j+3]=='URL':
            values[1].append(i[j:j+5])     
    pages[key]=values

importance={}
for i in pages:
    pages[i][1]=list((set(pages[i][1])))
    links=len(pages[i][1])
    init_importance=pages[i][0]/links
    
    for j in pages[i][1]:
        pages[j][0]+=init_importance
        
else:
    for i in pages:
        importance[i]=pages[i][0]

imp_val=list(importance.values())
imp_val.sort()
items_imp=importance.items()

final_ans=[]
for i in imp_val:
    for j in items_imp:
        if i==j[1] and j[0] not in final_ans:
            final_ans.append(j[0])
            
for i in final_ans[::-1]:
    print(i)