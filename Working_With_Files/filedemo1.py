"""

File I/O
'w' -> Write-Only mode
'r' --> Read-only Mode
'r+' --> Read and Write Mode
'a' --> Append Mode
"""

my_list = [1, 2, 3]

m_file = open("firstfile.txt", "w")

for item in my_list:
    m_file.write(str(item)+ "\n")

m_file.close()
