import math
t=int(input())
for x in range(t):
	p,s=list(map(int,input().split()))
	l= (p-math.sqrt(p*p-24*s))/12
	v=l*s/2-l*l*p/4+l*l*l
	print("%.2f" % v)