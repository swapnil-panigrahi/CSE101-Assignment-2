wts = [(10, 5), (20, 5), (100, 15), (40, 10), (20, 10), (40, 20), (70, 35)]

with open("CSE101-Assignment-2\IPmarks.txt","r") as F:
    file=F.readlines()

marks={}

for i in file:
    j=i.strip().split(',')
    marks[int(j[0])]=list(map(int,j[1:]))

student=[]
for i in marks:
    final_marks=[]
    for j in range(len(marks[i])):
        final_marks.append(marks[i][j]/wts[j][0]*wts[j][1])
    else:
        values=[]
        values.append(sum(final_marks))
        
        if sum(final_marks)>=80:
            grade='A'
        elif sum(final_marks)>=70:
            grade='A-'
        elif sum(final_marks)>=60:
            grade='B'
        elif sum(final_marks)>=50:
            grade='B-'
        elif sum(final_marks)>=40:
            grade='C'
        elif sum(final_marks)>=35:
            grade='C-'
        elif sum(final_marks)>=30:
            grade='D'
        else:
            grade='F'
        
        values.append(grade)
        student.append([i]+values)

F=open("CSE101-Assignment-2\IPgrades.txt",'w')
for j in student:
    F.write(str(j).strip(']').strip('[')+"\n")
F.close()