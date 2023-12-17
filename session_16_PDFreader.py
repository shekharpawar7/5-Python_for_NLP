#from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader 
reader=PdfReader("python_tutorial.pdf")

#find the length of pdf
print(len(reader.pages)) #28

#acces spcific page
page=reader.pages[5]
page

#extracting text from page --------------acces data of 5 page  
text=page.extract_text()
text
