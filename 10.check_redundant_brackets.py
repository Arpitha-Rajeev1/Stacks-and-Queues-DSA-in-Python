#For a given expression in the form of a string, find if there exist any redundant brackets or not. It is given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.
#A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.
#Example:
#Expression: (a+b)+c
#Since there are no needless brackets, hence, the output must be 'false'.

#Expression: ((a+b))
#The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.



from sys import stdin


def checkRedundantBrackets(expression):
	s = []
	count = 0
	for char in expression:
		if char != ')':
			s.append(char)
		else:
			if(not s):
				return True
			while s:
				ele = s.pop()
				if ele != '(':
					count += 1
				else:
					if count <= 1:
						return True
					else:
						count = 0
					break
	return False

expression = stdin.readline().strip()

if checkRedundantBrackets(expression):
	print("true")
else:
	print("false")
