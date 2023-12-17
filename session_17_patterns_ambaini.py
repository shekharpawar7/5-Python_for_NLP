string="""Name: Mukesh Ambani
Born: 19 April 1957 (age 66 years), Aden, Yemen
Net worth: 9,150 crores USD (2023) Forbes
Children: Anant Ambani, Akash Ambani, Isha Ambani
Spouse: Nita Ambani (m. 1985)
Education: Institute of Chemical Technology (ICT), St. Xavier's College (Autonomous), Hill Grange High School
Parents: Dhirubhai Ambani, Kokilaben Ambani
Siblings: Anil Ambani, Nina Kothari, Deepti Salgaocar"""

import re
def match_data(pattern,string):
    match=re.findall(pattern, string)
    if match:
        return match[0]

#acces name
match_data("Name\: ([A-Za-z ]*)", string)  #Mukesh Ambani

#acces birth data
match_data("Born\: ([1-9A-Za-z ]*)", string) #19 April 1957

#acces age 
match_data("\(age ([1-9]*)", string)  #66

#acces birth place
match_data("\(age [1-9]*\ [a-zA-z]*\), ([a-zA-Z, ]*)", string) #Aden, Yemen


#..............................................................................

def person_information(string):
    name=match_data("Name\: ([A-Za-z ]*)", string)
    date=match_data("Born\: ([1-9A-Za-z ]*)", string)
    age=match_data("\(age (\d{2})", string)
    palce=match_data("\(age [1-9]*\ [a-zA-z]*\), ([a-zA-Z, ]*)", string)
    return{"Name":name,"Birth_date":date,"Age":int(age),"Birth_palce":palce}

person_information(string)
"""output:   {'Name': 'Mukesh Ambani',
             'Birth_date': '19 April 1957 ',
             'Age': 66,
             'Birth_palce': 'Aden, Yemen'}"""



