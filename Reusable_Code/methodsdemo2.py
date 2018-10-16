"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needd in the code
"""

def sum_nums(n1, n2):
	"""
	Get sum of two numbers
	"""
	return n1 + n2
	

sum1 = sum_nums(2, 8)

sum2 = sum_nums(3, 3)

string_add = sum_nums('one', 'two')
print(string_add)

print(sum1)
print(sum2)
print("*"*20)

def isMetro(city):
	l = ['sfo', 'nyc', 'chi']
	
	if city in l:
		return True
	else:
		return False

x = isMetro('sfo')
print(x)

