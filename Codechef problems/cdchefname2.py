import re
t=int(input())
for x in range(t):
	n,z=[],[]
	m,w=(input().split())
	if len(m)<=len(w):
		for i in range(len(m)):
			h=re.findall(m[i],w)
			n.append(h)
			n2=list(filter(None,n))
		print('YES' if len(n2)== len(m) else 'NO')	
	else :
		for k in range(len(w)):
			j=re.findall(w[k],m)
			z.append(j)
			z2=list(filter(None,z))
		print('YES' if len(z2)== len(w) else 'NO')
	



	# if(len(n2)== len(m)):
		# 	print("YES")
		# else:                
		# 	print("NO")
		# if(len(z2)==len(w)):
		# 	print("YES")
		# else:
		# 	print("NO")
			







# t=int(input())
# for x in range(t):
# 	m,w=list(map(str,input().split()))
# 	if m.count(w)>0 or w.count(m)>0:
# 		print("YES")
# 	else :
# 	
	# print("NO")	
