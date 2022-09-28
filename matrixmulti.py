x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[2,1,1],[4,1,2],[1,1,1]]
R=[[0,0,0],[0,0,0],[0,0,0]]
print("first matrix is",x)
print("second matrix is ",y)
for i in range(len(x)):
	for j in range(len(x[0])):
		for k in range(len(y)):
			R[i][j]+=x[i][k]*y[k][j]
print("resultant matrix")
for r in R:
	print(r)

