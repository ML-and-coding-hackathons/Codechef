def nfn():
		g=len(n)-1
		i=0	
		n.remove(g)
		print(max(n))

t=int(input())
for x in range(t):
	# n=[]
	n=list(map(int,input().split()))
	nfn()	
	
	# print(g)
# del n[i]
	# print(n)