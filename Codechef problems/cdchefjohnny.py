u=int(input())
for l in range(u):  #numb of cases
    N=int(input())#numm of variables 
    a=list(map(int,input().split()))#value of variab
    K=int(input())
    x=a[K-1]
    a.sort()
    print(a.index(x)+1)
  
