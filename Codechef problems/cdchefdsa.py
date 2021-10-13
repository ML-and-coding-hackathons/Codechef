# T=int(input())
# for x in range(T):
# 	res=[]
# 	n=int(input())
# 	for y in range(n):
# 		s,p,v=list(map(int,input().split()))
# 		q=int(int(p/(s+1))*v)
# 		res.append(q)
# 	print(max(res))

# import re
# T=int(input())
# for x in range(T):	
# 	res=str(input())
# 	z=re.match('^>',res)
	
# 	c1=0
# 	c2=0
# 	for x in res:
# 		if x=='<':
# 			c1+=1
# 		if x=='>':
# 			c2+=1
# 	slist=list(res)		
# 	if  z==None:
# 		if c2>c1:
# 			c=c2-c1

# 			print(len(slist[:-c]))

# 		if c2==c1:
# 			print(c2+c1)	


# 	else:
# 		print(0)
	# print(z)





T=int(input())
for x in range(T):
	k,q=map(int,input().split())
	
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	s=[]
	for z in a:
		for zz in b:
			s.append(z+zz)
			s.sort()

	for l in range(q):

		c=int(input())		
	
		print(s[c-1])		

