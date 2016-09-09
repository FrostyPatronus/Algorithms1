import merge as m

def merge_sort(array):
	array_len = len(array)
	array_1 = array[0 : array_len // 2]
	array_2 = array[array_len // 2 : ]

	if array_1 == [] or array_2 == []:
		return m.merge(array_1, array_2)
	
	print array_1, array_2
	
	return m.merge(merge_sort(array_1), merge_sort(array_2))
