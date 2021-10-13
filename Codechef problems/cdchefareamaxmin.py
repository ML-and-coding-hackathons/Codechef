import numpy as np
t=int(input())
Area=[0]*t

for c in range(t):
	x1,y1,x2,y2,x3,y3=list(map(int,input().split()))
	Area[c] = (abs(float((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)))
	mxx=max(Area)
	mnn=min(Area)
	mx=2*max(Area)
	mn=0
	if mxx >= m:
		pass


# mx=Area.index(max(Area))
# mn=Area.index(min(Area))
# # print(Area)
# print(mn+1,mx+1)


# mxInx = np.argmax(Area)

# mnInx = np.argmin(Area)

# print(mxInx,mnInx)

#print("Max Area=",str(mxInx[-1]))


#print("Min Area=",str(mnInx[-1]))


# we need to find indices from general inputs'-max area and min  at that index nums







# def area(a1,b1,a2,b2,a3,b3):
#     return float(abs(a1*(b2-b3)+a2*(b3-b1)+a3*(b1-b2)))/2
# ma=0
# mi=1000000000000000
# posma=0
# posmi=0
# for i in xrange(1,input()+1):
#     x1,y1,x2,y2,x3,y3=(map(int,raw_input().split()))
#     c=area(x1,y1,x2,y2,x3,y3)
#     #print c
#     if ma<=c:
#         ma=c
#         posma=i
#     if mi>=c:
#         mi=c
#         posmi=i
# print posmi,posma
#     