from itertools import permutations,chain,combinations
T=int(input())
for l in range(T):
	N=int(input())  #charctrs in th string
	S,X=list(map(str,input().split()))
	x=list(chain(*[combinations(S,x) for x in range(1,len(S)+1)]))
	# x=list(combinations(S,r))
	# x=list( for x in range(1,len(S)+1)]))
	q=0
	for d in x:
		if X in d:
			q+=1
			
	print(q)
	# print(x)
# hjg h -h,hj,hg,hjg
