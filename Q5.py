N=int(input("Enter the rows of matrix for scaling: "))

matrix=[]
for i in range(N):
    x,y=map(float,input("Enter the coordinates: ").strip().split())
    matrix.append([x,y,1])

print("Your matrix will be scaled by \n|cx 0 0|\n|0 cy 0|\n|0  0 1|")

cx=float(input("Enter cx: "))
cy=float(input("Enter cy: "))

scaling=[[cx,0,0],[0,cy,0],[0,0,1]]

for i in range(len(matrix)):
    matrix[i][0]*=cx
    matrix[i][1]*=cy

print([[i[0],i[1]] for i in matrix])