def fib(length):
	first = 1
	second = 1
	if length == 0:
		return 0
	elif length <= 2:
		return 1
	else:
		length -= 2
		for i in range(length):
			temp = first
			first = second
			second = temp+first
		return second
