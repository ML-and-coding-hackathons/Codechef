
n,x,y=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))

l1=[0]*x
l2=[0]*y
c=[]

if x==0 or y==0:
	for i in range(n):
		try:
			if a[i]>b[i]:
				l1[i]=(a[i])

			elif a[i]==b[i]:
				l2.append(b[i])

			else:	
				l2[i]=(b[i])
		except IndexError:
			pass

else:
	for q in range(n):
		if a[q]>=b[q]:
			l1.append(a[q])
		else:
			l2.append(b[q])


			 			
c=l1+l2
print(sum(c))		
