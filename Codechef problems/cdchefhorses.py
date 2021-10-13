# for x in range(int(input())):
#     N=int(input())
#     S=list(map(int,input().split()))
#     S.sort()
# print (S)    

for l in range(int(input())):  #numb of cases
    N=int(input()) #numm of variables
    S=list(map(int,input().split()))#value of variab
    S.sort()
    k=S[1]-S[0]
    for i in range(1,N-1):
        if k > S[i+1]-S[i]:
        	k=S[i+1]-S[i]
    print(k)    