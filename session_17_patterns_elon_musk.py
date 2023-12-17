string="""Born: 28 June 1971 (age 52 years), Pretoria, South Africa
Net worth: 21,900 crores USD (2023) Forbes
Children: Vivian Jenna Wilson, Nevada Alexander Musk, Griffin Musk, Damian Musk, Kai Musk, Saxon Musk
Spouse: Talulah Riley (m. 2013–2016), Talulah Riley (m. 2010–2012), Justine Musk (m. 2000–2008)
Full name: Elon Reeve Musk
Parents: Errol Musk, Maye Musk"""

#acces alon musk birth data
import re
pattern="age [1-9]* [a-z]*"
match=re.findall(pattern, string)
match  #  ['28 June 1971']

#acces age
pattern="age (\d{2}) [a-z]*"
match=re.findall(pattern, string)
match #   52

def match_pattern(pattern,string):
    match=re.findall(pattern, string)
    if match:
        return match[0]
 
#acces age
match_pattern("age (\d{2}) [a-z]*", string)

pattern="Born\: (\d{2} [A-Za-z]* [1-9]*)|age \d{2}* [a-z]*"
match=re.findall(pattern, string)
match

#acces date and age
match_pattern("Born\: (\d{2} [A-Za-z]* [1-9]*) \(age ([1-9]*) [a-zA-Z]*\)", string)

#acces name
match_pattern("name\: ([A-Za-z ]*)", string)

#birthplace
match_pattern("age \d{2} [a-z]*\)\, ([a-zA-Z \,]*)", string)



#......................................................................................


string="""Born: 28 June 1971 (age 52 years), Pretoria, South Africa
Net worth: 21,900 crores USD (2023) Forbes
Children: Vivian Jenna Wilson, Nevada Alexander Musk, Griffin Musk, Damian Musk, Kai Musk, Saxon Musk
Spouse: Talulah Riley (m. 2013–2016), Talulah Riley (m. 2010–2012), Justine Musk (m. 2000–2008)
Full name: Elon Reeve Musk
Parents: Errol Musk, Maye Musk"""


def person_info(string):
    name=match_pattern("name\: ([A-Za-z ]*)", string)
    born=match_pattern("Born\: (\d{2} [A-Za-z]* [1-9]*)",string)
    age=match_pattern("age (\d{2}) [a-z]*", string)
    palce=match_pattern("age \d{2} [a-z]*\)\, ([a-zA-Z \,]*)", string)
    return{"name":name,"Birth_date":born,"Age":int(age),"birth_palce":palce}
        
person_info(string)  
"""output:'
1
1name': 'Elon Reeve Musk',
         'Birth_date': '28 June 1971',
         'Age': 52,
         'birth_palce': 'Pretoria, South Africa'}
    """
#.....................................................................................
