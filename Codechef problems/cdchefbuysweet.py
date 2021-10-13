u=int(input())
for l in range(u):
	n,x = list( map( int, input().split()))
	s = list( map( int, input().split()))
	k=sum(s)
	
	if (k%x==0):
		print(k//x)
	elif (n==1 and k>x) :
		print(1)
	else  :
		print(-1)	

	# print([k/x if (k%x==0) 1 if(n==1 and k>x)  else -1 ])	
 # 