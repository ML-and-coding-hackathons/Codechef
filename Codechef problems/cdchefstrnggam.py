t=int(input())
for x in range(t):
	n=int(input())
	ai=list(map(int,input().split()))[:n]
	di=list(map(int,input().split()))[:n]
	ai.sort()
	di.sort()
	if ((ai[n-1]+ai[n-2]) > (di[n-1]+di[n-2]) ): 
		print('AAYUSHI')
	else :
		print('DAKSH')
		

