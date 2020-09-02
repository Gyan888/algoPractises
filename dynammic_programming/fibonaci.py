def fibonaci(number):  # recursive approach for fibonaci
	if number == 0:
		return 0
	elif number == 1:
		return 1
	else:
		return fibonaci(number-1) + fibonaci(number-2)



def fibonaci2(number):		# fibonaci with memoization or dynamic approach
	global arr 				# this has performance advantage as compared to recursive approach
	if arr[number] != -1:
		return arr[number]
	else:		
		arr[number] = fibonaci2(number-1) + fibonaci2(number-2)

	return arr[number]




def fibonaci3(number):	# this has both performance and space its the best aproach
	a = 0
	b = 1
	if number==0:
		return 0
	elif number ==1:
		return 1
	else:
		for i in range(2, number+1):
			c = a + b
			a = b
			b = c			
		return b

number = 4
arr = (number+1)*[-1]
arr[0] = 0
arr [1] = 1
print(fibonaci2(number))
print("arr", arr)
