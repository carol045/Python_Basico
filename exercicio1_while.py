n = 2000
a, b = 0, 1

while a < n:
	print(a, end="\n")
	a, b = b, a+b

