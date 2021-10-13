import re
t=int(input())
for i in range(t): 
	a=int(input())
	x=str(input())
	

	if re.search('(100000+?)', x) or re.search('(0*1)', x) :
		if ("11"in x) or ("101" in x)  or ("1001" in x) or ("10001" in x) or ("100001" in x):
			print("NO")
		else:
			print("YES")
	else:
		print("NO")	