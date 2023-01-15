def splitatnum(x):
    for i in x:
        if i.isnumeric():
            y=x.partition(i)
            break
    return y[0],y[1]+y[2]

transcript=[]

print("Enter in the following format:{Course No.} {Number of credits} {Grade recieved}")
while True:
    record=input().strip()
    if record=="":
        break
    else:    
        transcript.append(record.split())

iterator=0
while iterator<len(transcript):
    
    i=transcript[iterator]
    
    if splitatnum(i[0])[0].isalpha() and splitatnum(i[0])[0].isupper() and splitatnum(i[0])[1].isnumeric() and int(i[1]) in [1,2,4] and i[2] in ("A+","A","A-","B","B-","C","C-","D","F"):
        print(i[0]+": "+i[2])
        iterator+=1
        
    elif int(i[1]) not in [1,2,4]:
        print("Invalid Credits")
        transcript.remove(i)
    
    else:
        print("Invalid Course Code")
        transcript.remove(i)
    
    if i[2] not in ("A+","A","A-","B","B-","C","C-","D","F"):
        print("Invalid Grade")
        transcript.remove(i)    

sgpa_calc=[]
total_credits=0
for i in transcript:
    if i[2]=="A+" or i[2]=="A":
        sgpa_calc.append(10)
    elif i[2]=="A-":
        sgpa_calc.append(9)
    elif i[2]=="B":
        sgpa_calc.append(8)
    elif i[2]=="B-":
        sgpa_calc.append(7)
    elif i[2]=="C":
        sgpa_calc.append(6)
    elif i[2]=="C-":
        sgpa_calc.append(5)
    elif i[2]=="D":
        sgpa_calc.append(4)
    else:
        sgpa_calc.append(2)
        
    total_credits+=int(i[1])

x=[sgpa_calc[i]*int(transcript[i][1])/total_credits for i in range(len(sgpa_calc))]

print("SGPA: ",round(sum(x),2))