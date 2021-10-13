
u=int(input())      	
for t in range(u):
	h = str(input())
	a="101"
	b="010"

	for l in h:
		if (h.count(a)>0) or (h.count(b)>0):
			print("Good")
			break
		else:
			print("Bad")	
			break


			# r=re.compile("(\101)")

			# m=re.search(r,l)
			# if m:
			# 	print('good')
			# else:
			# 	print('bad')
			# # if len(m) > 0 :
			# 		print('good')
   #  		else :
   #  				print('bad')	
    		# line =line.rstrip()
    		# x = re.findall("101", line)
    		




# import re
# tc=int(input())
# for i in  range(tc):
# 	feedb=str(input())
# 	searcher=re.compile('010|101')
# 	match=list(searcher.findall(feedb))
# 	if(len(match)==0):
# 		print("Bad")
# 	else:
# 		print("Good")