# Dynamic programming Longest Increasing subsequence


def lis(arr):
	n = len(arr)
	l = n*[1]
	for j in range(1, n):		
		for i in range(0, j):
			if arr[j]>arr[i] and l[j]<l[i]+1:
				l[j] = l[i]+1
	print(l)


arr = [100, 22, 9, 33, 21, 50, 41, 60] 
	
lis(arr)