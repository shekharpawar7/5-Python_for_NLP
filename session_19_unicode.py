str1="apple"
str2="jeei123"
str3="12345"
str4="pre@12"

str1.encode(encoding="UTF-8",errors="strict") #b'apple'
str2.encode(encoding="UTF-8",errors="strict") #b'jeei123'
str3.encode(encoding="UTF-8",errors="strict") #b'12345'
str4.encode(encoding="UTF-8",errors="strict") #b'pre@12'

text="one 🐘 and three 🐋"
print(text)
len(text) #17

code=text.encode("utf8")
code #b'one \xf0\x9f\x90\x98 and three \xf0\x9f\x90\x8b'


#..................................................................................
fname="data.txt"
with open(fname,mode='rb') as f:
    cont=f.read()
    print(type(cont))
    print(cont)
    print(cont.decode("utf8"))
    
"""<class 'bytes'>
b'one \xf0\x9f\x90\x98 and three \xf0\x9f\x90\x8b'
one 🐘 and three 🐋"""

#....................................................................................
