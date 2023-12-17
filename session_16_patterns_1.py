
import re
string="hi: i have problem with my order number 23456789"
pattern="order [a-z]* ([1-9]*)"
match=re.findall(pattern, string)
match #  ['23456789']

pattern="order [^\d]* ([1-9]*)"
match=re.findall(pattern, string)
match #  ['23456789']

#................................................................................
import re
string="hi: hello, i am having an issue with my order # 3456778"
pattern="order [^\d]* ([1-9]*)"
match=re.findall(pattern, string)
match

string="hi: hello my order is 234567890 and issue with them"
pattern="order [^\d]*([1-9]*)"
match=re.findall(pattern, string)
match

#function
import re
def match_patter(pattern,string):
    matches=re.findall(pattern, string)
    if matches:
        return matches[0 ]
    
match_patter("order [^\d]*([1-9]*)", string)    #'23456789'

#acces email from string
string="hello bro my eamil is shekharpawar0777@gamil.com"
pattern="[a-zA-Z]*[\d]*\@[a-z]*\.[a-zA-Z]*"
match=re.findall(pattern, string)
match  #shekharpawar0777@gamil.com