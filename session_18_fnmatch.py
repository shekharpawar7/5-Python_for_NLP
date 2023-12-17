from fnmatch import fnmatch
names=["dat1.csv","dat2.csv","config.ini","foo.py"]
[name for name in names if fnmatch(name,"*.csv")]
#['dat1.csv', 'dat2.csv']


addresses=["23423 N CLARL ST","2345 N SDFVB AVS","23423 N STWERG ST"]
from fnmatch import fnmatch
[addr for addr in addresses if fnmatch(addr,"*ST")]
#['23423 N CLARL ST', '23423 N STWERG ST'] 

lsit=["west mumbai","east mumbai","east andheri"]
[i for i in lsit if fnmatch(i,"*mumbai")]

text="yeah, but no ,but yeah"
text=="yeah"  #false
text.startswith("yeah") #Ture
text.endswith("yeah") #true


#...................................................................................
