from itertools import combinations 
t=int(input())
c=[]
for x in range(t):
	a=list(map(int,input().split()))
	c+=a
# 	
l=list(combinations(c,2))	
q=[];
for i in range(0,len(l)):
	b=int((sum(l[i]))/2)
	q.append(b)
flag=0

q=list(dict.fromkeys(q))
for ii in q:	
	if ii in c:
		flag+=1

print(flag)	