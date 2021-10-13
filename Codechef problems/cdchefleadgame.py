t=int(input())
a=[0]*t;y=[0]
a=[1]*t;z=[0]
for x in range(0,t):
	a[0],a[1]=list(map(int,input().split()))
	y.append(a[0])
	z.append(a[1])
y.pop(0)
z.pop(0)
# print(y)
# print(z)
i=0;r=[];l=0
for i in range(len(y)-1):
	y[i+1]+=y[i]
	z[i+1]+=z[i]
ww=0
# print(y,z)	
for i in range(len(y)):	
	r.append(abs(y[i]-z[i]))
	s=max(r)
	l=r.index(s)
	if y[l]>z[l]:
		ww=1
	else:
		ww=2	

print(ww,s)
