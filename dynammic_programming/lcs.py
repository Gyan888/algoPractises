text1 = "AGGTAB"
text2 = "GXTXAYB"


# lowest common subsequence recursive approach 
#complexity for this approach is 2^n


def LCS(X, Y, i, j):
	print ("check for negative i: {}, j: {}".format(i, j))
	if(i==0 or j==0):
		return 0
	elif X[i-1] is Y[j-1]:
		return 1 + LCS(X, Y, i-1, j-1)
	else:
		return max(LCS(X, Y, i-1, j), LCS(X, Y, i, j-1))




################# dynamic approach for  solving longest common subsequesnce 
#complexity for this approach is m*n


def LCS_dynammic(X, Y):
	m = len(X)
	n = len(Y)
	L = [[None]*(n+1) for i in range(m+1)]	
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j]=0
			elif X[i-1] == Y[j-1]:				
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	return L[m][n]

print ("Longest subsequence {}".format(LCS_dynammic(text1, text2)))
