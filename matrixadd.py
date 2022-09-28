x=[[12,7,3],
  [4,5,6],
  [7,8,10]]
  
y=[[5,8,1],
  [6,7,4],
  [4,5,6]]
  
z=[[0,0,0],
   [0,0,0],
   [0,0,0]]
   
for i in range(len(x)):
	
	for j in range(len(x[0])):
		z[i][j]=x[i][j]+y[i][j]
		
print("matrix x:")
for r in x:
	print(r)
print("matrix y:")
for r in y:
	print(r)
print("resultant matrix:")
for r in z:
	print(r)
