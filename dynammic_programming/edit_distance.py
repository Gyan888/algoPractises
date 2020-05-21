# there are two strings we have to figure out minimum number of operations required to make them equal
# set of operations that can be performed are 1)Insertion 2)deletion 3)Substitution and each of these
# operation has a weightage of 1 

s1="sunday"
s2="saturday"

# recursive approach of solving the problem 
# comlexity for this approach is 3^n  as there is lot of repetation in, we can use memoization or dynamic aproach


def min_distance(s1, s2, m, n):
	if m == 0: 
		return n
	elif n == 0:
		return m
	elif s1[m-1] == s2[n-1]:
		return min_distance(s1, s2, m-1, n-1)
	else:
		return 1 + min(min_distance(s1, s2, m-1, n-1), # replace
			   	 	   min_distance(s1, s2, m-1, n), # insert 
			   	   	   min_distance(s1, s2, m, n-1)) # remove


print ("this is it {}".format(min_distance(s1, s2, len(s1), len(s2))))
	

# dynamic aproach of solving the problem 
# complexity for this aproach is m*n

def min_distance_dynamic(s1, s2):
	m = len(s1)
	n = len(s2)
	l = [(n+1)*[None] for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):			
			if i is 0:
				l[i][j] = j
			elif j is 0:
				l[i][j] = i
			elif s1[i-1] == s2[j-1]:
				l[i][j] = l[i-1][j-1]
			else:
				l[i][j] = 1 + min(l[i-1][j], l[i][j-1], l[i-1][j-1])
			
	print ("Matrix formed {}".format(l))
	return l[i][j]


print ("this is it {}".format(min_distance_dynamic(s1, s2)))
