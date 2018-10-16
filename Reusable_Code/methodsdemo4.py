"""
Variable Scope
"""

a = 10
"""
def test_method(a):
	print("Value of local a is: " + str(a))
	a = 2
	print("New value of local a is: " + str(a))

print("Value of global a is: " + str(a))
test_method(a)
print("Did the value of global a change: " + str(a))
"""
a = 10

def test_method(a):
	global a
	print("Value of local a is: " + str(a))
        
	a = 2
        print("New value of local a is: " + str(a))

	print("Value of global a is: " + str(a))

print("Value of global a is: " +str(a))
test_method(a)



