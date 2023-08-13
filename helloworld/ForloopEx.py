small = None
print('Before Loop:', small)
for x in [12, 0, 21,-3]:
	if small is None or x < small :
		small = x
	print('Iteration Variable:', x, 'small:', small)
print('Smallest:', small)
