#stripping
s='   hello world  \n'
s.strip()  #    'hello world'

s.lstrip()  #   'hello world  \n'

s.rstrip()  #   '   hello world'

#...............................................................................
s="------hello world========"
s.strip("-")  # 'hello world========'

s.strip("=")  #'------hello world'

s.strip("-=")  #'hello world'

#..................................................................................
s="hello world          "

s.strip()            #'hello world'

s.replace(" ", "")   #'helloworld'

import re
re.sub("\s*","",s)  #'helloworld'
