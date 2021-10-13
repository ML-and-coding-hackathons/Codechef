import math
T=int(input())
for x in range(T):
	X,Y=list(map(int,input().split()))				
 	
	print(2*(math.gcd(X,Y)))



# T=int(input())
# for x in range(T):
# 	X,Y=list(map(int,input().split()))
# 	if(X == Y):
# 		print(X+Y)

# 	elif(X<Y):
# 		Y=Y%X
# 		if(Y):
# 			print(Y)
# 		else:
# 			print(2*X)
# 	else:
# 		X=X%Y
# 		if(X):
# 			print(X)
# 		else:
# 			print(2*Y)				