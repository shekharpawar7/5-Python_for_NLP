
s1="Spicy Jalape\u00f1o"
s2="Spicy Jalapen\u0303o"
s1==s2
#false

import unicodedata
t1=unicodedata.normalize("NFC",s1)
t2=unicodedata.normalize("NFC",s2)
t1==t2
#True