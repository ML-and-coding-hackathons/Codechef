from itertools import groupby 
t=int(input())
x=0;
y=0;
for i in range(t):
	a=int(input())
	b=str(input())
	b=b.replace('LR','L')
	b=b.replace('RL','R')
	b=b.replace('UD','U')
	b=b.replace('DU','D')
	b=b.replace('LL','L')
	b=b.replace('RR','R')
	b=b.replace('DD','D')
	b=b.replace('UU','U')
	if  'L' in b :
		x=x-1
		
	if  'R' in b :
		x=x+1
			
	if 'U' in b :
		
		y=y+1
	if  'D' in b :
		
		y=y-1		

	print(x,y)		