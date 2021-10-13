from itertools import combinations
# import time

    
t=int(input())
for x in range(t):
	n,k=list(map(int,input().split()))
	r=[0]*(n-1)
	# start = time.time()
	print(len(list(combinations(r,k-1))))
	

# "the code you want to test stays here"
# end = time.time()
# print(end - start)