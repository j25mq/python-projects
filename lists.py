def total_length(list):
	total = 0
	for string in list:
		total = total + len(string)
	return total

print(total_length(['foo', 'bar']))
print(total_length([]))
print(total_length(['balloons']))
print(total_length(["", '', "", '']))