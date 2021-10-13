t=int(input())
for x in range (t):
	a=[0]*5
	a[0],a[1],a[2],a[3]=list(map(int,input().split()))
	z=a[0]*a[2]
	y=a[1]*a[3]
	if (z+y)%2==0:
		print('YES')
	else :
		print('NO')	