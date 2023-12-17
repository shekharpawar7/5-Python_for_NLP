string="welcome to the 2024"
x=string.split()
x

#................................................................................
#remove spcial char
string="007 Not sure@ if this %was # fun!"
import re
def remove_spcial(string):
    pattern="[^a-zA-Z0-9\s]" #only this chr can present all are  remove
    return re.sub(pattern,"", string)
    

remove_spcial("007 Not sure@ if this %was # fun!") 
#007 Not sure if this was  fun

#............................................................................
#remove number
string="00345677 Not sure@ if this %was # fun!"
def remove_num(string):
    pattern="[^A-Za-z,.;:@#\s]"
    return re.sub(pattern,"", string)
remove_num(string) #Not sure@ if this was # fun

#..............................................................
#remove ";"

string="welcome: to the, new year; 2021"
match=re.sub(";","", string)
match  #  welcome: to the, new year 2021

#.......................................................................................
#removing punctuation
import string
def re_punctuation(st):
    text="".join([c for c in st if c not in string.punctuation])
    return text


re_punctuation("artical: @first sentence of same , artical")

