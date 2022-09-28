from math import sqrt
import numpy as np
import random
ran=[]
n=12
for i in range(n):
	ran.append(random.randint(1,10))
print("random numbers:",ran)
mean=np.mean(ran)
print("mean:",mean)
varience=np.var(ran)
sd=sqrt(varience)
print("sd:",sd)
