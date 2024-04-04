from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack):
	if (len(inputStack) <= 1):
		return
	while(len(inputStack) != 1):
		ele = inputStack.pop()
		extraStack.append(ele)
	lastElement = inputStack.pop()

	while (len(extraStack) != 0):
		ele = extraStack.pop()
		inputStack.append(ele)
	reverseStack(inputStack, extraStack)
	inputStack.append(lastElement)


def isEmpty(stack):
	return len(stack) == 0


def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")
