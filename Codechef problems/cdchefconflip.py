t=int(input())
for l in range(t):  #numb of cases
    g=int(input())#numm of games 
    for r in range(g):
    	i,n,q=list(map(int,input().split()))
    	
    	if (n%2==0 or i==q):
    		print(n//2)
    	else :
    		print((n//2)+1)
    				
  
