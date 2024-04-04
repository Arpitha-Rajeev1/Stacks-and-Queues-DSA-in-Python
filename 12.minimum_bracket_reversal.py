#For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
#If the expression can't be balanced, return -1.
#Example:
#Expression: {{{{
#If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

#Expression: {{{
#In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.
#Sample Input 1:
#{{{
#Sample Output 1:
#-1
#Sample Input 2:
#{{{{}}
#Sample Output 2:
#1
  
from sys import stdin

def countBracketReversals(inputString) :
    if len(inputString) %2 != 0:
        return -1
    s = list()
    for char in inputString:
        if char == '{':
            s.append(char)
        elif char == '}':
            if not s:
                s.append('}')
            else:
                ele = s[-1]
                if ele == '{':
                    s.pop()
                else:
                    s.append(char)
    if not s:
        return 0
    count = 0
    while s:
        c1 = s.pop()
        c2 = s.pop()
        if c1 == c2:
            count += 1
        else:
            count += 2
    return count


print(countBracketReversals(stdin.readline().strip()))
