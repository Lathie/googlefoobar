#def thing(x):
#	return recur(x, 0, 1, list())
	
#def recur(left, right, cur, list):
#	if (left == right):
#		return list;
#	elif (left + cur - right) % (cur * 3) == 0:
#		list.append('L')
#		recur(left + cur, right, cur*3, list)
#	elif (right + cur - left) % (cur * 3) == 0:
#		list.append('R')
#		recur(left, right + cur, cur*3, list)
#	else:
#		list.append('-')
#		recur(left, right, cur*3, list)
		
def thing(x):
	left = x
	right = 0
	cur = 1
	
	while (left != right):
		if (left + cur - right) % (cur * 3) == 0:
			print("left")
			left += cur
			
		elif (right + cur - left) % (cur * 3) == 0:
			print("right")
			right += cur
			
		else:
			print("-")
			
		cur *= 3
	
thing(3)
thing(7)
thing(10)
thing(13)
thing(16)
thing(18)
thing(21)
