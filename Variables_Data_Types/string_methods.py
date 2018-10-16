"""
Examples to show available string methods in python
"""

# Accessing characters in a string
# index starts from zero
first = "nyc"[2]
city = "sfo"
print(first)
ft = city[0]
print(ft)

"""
len()
lower()
uppder()
str()

"""

stri = " This Is a  Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))

"""
concatenantion
"""

print("Hello"+" " + " " + "World!!")
print(first + " " + city)
