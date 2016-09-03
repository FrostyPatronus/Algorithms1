# takes two sorted lists of numbers and produces a list that combines them that is sorted. 
# The merge part in merge sort

one = raw_input("LIST ONE\n").split()
two = raw_input("LIST TWO\n").split()

c = []

for s in range (0, len(one) + len(two)):	
	if not (one and two):
		if not one:
			c.extend(two)
		else:
			c.append(one)
		break

	if one[0] < two[0]:
		c.append(one.pop(0))
	else:
		c.append(two.pop(0))

print c