t=int(input())
for x in range(t):
	a=int(input())
	b=list(map(int,input().split()))
	c=[]
	for y in range(len(b)):
		b[y]=b[y]-y
		c.append(b[y])
	print(sum(c))	
