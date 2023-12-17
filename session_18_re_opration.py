import re
text="27/12/2020" #YES
if re.match("\d*\/\d*\/\d*",text) and re.match("\d{2}\/\d{2}\/\d{4}",text):
    print("yes")
else:
    print("no")
    
text1="20 Nov 2020"  #No
if re.match("\d*\/\d*\/\d*",text1):
    print("yes")
else:
    print("no")
    
#........................................................................................................
#.compile()
datepat=re.compile("\d{2}\/\d{2}\/\d{4}")
if re.match(datepat,text):
    print("yes")
else:
    print("no")
    
datepat=re.compile("\d{2}\/\d{2}\/\d{4}")
if re.match(datepat,text1):
    print("yes")
else:
    print("no")
    
#..............................................................................
text="yeah,but no,but yeah,but no,but yeah"
text.replace("yeah","yeep") #'yeep,but no,but yeep,but no,but yeep'

#................................................................................
#convert date fromat
text="today is 11/27/2020. Pycom start 3/13/2020"
import re
re.sub(r"(\d*)/(\d*)/(\d*)",r"\3-\2-\1",text) 
#subtutution-(old pattern,new patten,string)
#                           |
#                           | 
                #3rd grp__2nd grp__1st grp


#...........................................................................................
#ignaor the case type
text="UPPER PYTHON,lower python,Mixed Python"
re.findall("python",text,flags=re.IGNORECASE)    

#replace
#ignaor the case type
text="UPPER PYTHON,lower python,Mixed Python"
re.sub("python","sanke",text,flags=re.IGNORECASE)  
#  re.sub(old      , new   ,string)
   
#use function and replace with case type
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace 
text3=re.sub("python",matchcase("sanke"),text,flags=re.IGNORECASE)
text3        

#...........................................................................................
str_pat=re.compile("\"(.*)\"")
text1="computer says no."
str_pat.findall(text1)
import re
text="Computer says no. Phone says yes."
str_pat=re.compile(r'\"(.?)\"')
str_pat.findall(text1)

#aaces data from comment
text="/* this is a comment */"
match=re.findall(r"\/\* ([A-Za-z ]*) \*\/", text)                   
match

#mutiline comment
text="""/* this is a
multiline comment */"""
match=re.findall(r"\/\* ([a-zA-Z \n]*) \*\/", text)
match #['this is a\nmultiline comment']

text="""/* this is a
multiline ;comment */"""
str_pat=re.compile(r"\/\* ([a-zA-Z\,\;\: \n]*) \*\/",re.DOTALL)
str_pat.findall(text)
#['this is a\nmultiline ;comment']

















