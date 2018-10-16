""" 
Examples to show strings
"""

a = "1abc2abc3abc4abc"
print(a.replace("abc", "ABC", 1))

# Sub-Strings
# Starting index is inclusive
# Ending index is exclusive
sub = a[1:6:2]
step = a[1:6]
print("**********************")

print(sub)
print(step)
