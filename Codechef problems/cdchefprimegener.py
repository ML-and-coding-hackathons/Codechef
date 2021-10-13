t=int(input())
w=[]
for x in range(t):
	m,n=list(map(int,input().split()))
	for w in range(m,n+1):
		if w>1:
			for r in range(2,w):
				if (w%r)==0 :
					break
			else :
				print(w)	
					
		

