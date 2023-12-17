#aligning text
text="hello world"
text.ljust(20)  #'hello world         '

text.rjust(20)  #'         hello world'

text.center(20) #'    hello world     '

#................................................................................
text="hello world"
text.ljust(20,"=")  #'hello world========='

text.rjust(20,"=")  #'=========hello world'

text.center(20,"=") #'====hello world====='

#................................................................................
text="hello world"

format(text,">20")  #'         hello world'
 
format(text,"<20")  # 'hello world         '

format(text,"^20")  #'    hello world     '

#...............................................................................
text="hello world"

format(text,"=>20")  #'=========hello world'
 
format(text,"*<20")  #'hello world*********'

format(text,"*^20")  #'****hello world*****'

#.....................................................................................
"{:>10s} {:>10s}".format("hello","world") # '     hello      world'


x="2.34534"
format(x,">10") #'   2.34534'

format(x,"^10.2f")

#.............................................................................................
#.join()
part=["is","Chicago","Not","Chicago"]
" ".join(part) # 'is Chicago Not Chicago'

".".join(part) #'is.Chicago.Not.Chicago'

",".join(part) #'is,Chicago,Not,Chicago'

#..............................................................................
a="my name"
b="shekhar"
c=a+b
c
