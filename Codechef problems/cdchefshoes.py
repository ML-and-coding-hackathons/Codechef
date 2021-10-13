t=int(input())
for x in range(t):
	q=list(map(int,input().split()))
	w=list(map(str,input().split()))
	t=0;y=0;
	if 'a' in w:
		t+=1
	if 'b' in w:
		y+=1		

	print(x,y)	