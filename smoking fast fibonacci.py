# %timeit -n 100 fib(10000)
# 100 loops, best of 3: 3.79 ms per loop

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
