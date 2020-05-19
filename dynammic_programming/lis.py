# Dynamic programming Longest Increasing subsequence


def lis(arr):
	n = len(arr)
	l = n*[1]
	for j in range(1, n):		
		for i in range(0, j):
			if arr[j]>arr[i] and l[j]<l[i]+1:
				l[j] = l[i]+1
	print(l)

# another array of 1 is used to add weightage of previous sequence so that we can judge if adding the previous number 
# is good enough or not better analyse it and use this method, previous increasing weight is added in current index
# and analysed which series is better gaining weight with current index 

arr = [100, 22, 9, 33, 21, 50, 41, 60] 
	
lis(arr)
