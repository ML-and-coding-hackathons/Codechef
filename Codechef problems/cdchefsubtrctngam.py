import math
T=int(input())
for x in range(T):
	a=int(input())
	X=list(map(int,input().split()))
	q=math.gcd(X[0],X[1])

	if(len(X)==2): 
		print(q)
	else:
		for i in range(2,len(X)):
			q=math.gcd(q,X[i])
		print(q)
		