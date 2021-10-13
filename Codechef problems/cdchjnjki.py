A,N,K = list( map( int, input().split()))
# A, N, K ,l = t[0], t[1], t[2], []
l=[]
for i in range(K):
    rem = A % (N+1)
    A = A /(N+1)
    l.append(int(rem))    
    
print(*l)    