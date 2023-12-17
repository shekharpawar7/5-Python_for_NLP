#slicing a string
s="ADHWFGHJKGFDSA"
s[2:7] #HWFGH--------------2to6

s="ASDFGHJKL"
s[-6:-2]   #start:end------(-6 to -2)  FGHJ

s="ASDFGHJKL"
s[2:-2] #'DFGHJ'

s="WERTYSDFGHJKLUIOP"
s[2:7:2]  #----------------RYDQQA

S="ASDFGHJKL" 
S[6:1:-2]  #------JGD

S="ABCDEF"
S[:3]    #--------ABC

S="WERTYUIOP"
S[3:]  #--------YUIOP

s="ASDFGHJKL"
s[::-1]  #...............LKJHGFDSA

filename="file.text"
filename[-5:]==".text"  # True

url="http://www.python.com"
url[:5]
url[:5]=="http:" or url[:6]=="https:" or url[:4]=="ftp:"







