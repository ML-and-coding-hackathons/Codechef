t=int(input())
for i in range(t):
	q=int(input())
	x=str(input())
	import re
	x = re.sub(r'[^\w\s]','',x) #removes dot from sentence
	# print(x)
	count=0
	cntT=0
	if re.search('^H', x):
		if re.search('[HT]',x):
			print('Valid')
		# for i in x:
			
			# if i=='HT':
			# 	count+=1
			# if i=='T':
			# 	cntT+=1
		# if count==cntT:
		# 	print('Valid')
		# else:
			# print('Invalid')					
	elif not x:
		print('Valid')

				

	else:
		print('Invalid')	
















# conditions:
# -for every h a t needed
# -t cannot initiate in string
# -'.' to be excluded with help of re
