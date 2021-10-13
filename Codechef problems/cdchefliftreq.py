import numpy as np
t=int(input())
for i in range(t):
	p=[0]*2;b=[0];
	p[0],p[1]=list(map(int,input().split()))
	a=[0]*2;c=[0]
	for j in range(0,p[1]):
		a[0],a[1]=list(map(int,input().split()))
		b.append(a[0])
		b.append(a[1])
	
	c=np.diff(b)
	print(sum(abs(c)))

	
	