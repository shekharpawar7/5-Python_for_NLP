import re
string="""Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion"""
pattern="\d\d\d\d\d\d\d\d\d\d"  #\d---accses digit from text
matches=re.findall(pattern,string)
matches  #9991116666

import re
string="""Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion"""
pattern="\d{10}"   #\d{10} it return 10 time \d
matches=re.findall(pattern,string)
matches  #9991116666

import re
pattern="\(\d\d\d\)\-\d\d\d\-\d\d\d\d"  #use \ to spacial symbol
match=re.findall(pattern, string)
match   #['(999)-333-7777']

pattern="\D\d\d\d\D\D\d\d\d\D\d\d\d\d"  #\D-----accses the non-Digit 
match=re.findall(pattern, string)
match   #['(999)-333-7777']


#acces both patttenr
pattern="\d{10}|\(\d{3}\)\-\d{3}\-\d{4}"
match=re.findall(pattern,string)
match

#........................................................................................
import re
#if we not need ; or any social_char use [^spacial_char]
string="""A protracted; legal battle; over a 32-carat;
 Golconda diamond-"""
pattern="[^;-]" #acces string without ; and -
match=re.findall(pattern, string)
match

#................................................................................................

import re
string="""Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
"""
pattern="Note \d \D [^\n]*" #acces data upto new line (\n)
match=re.findall(pattern,string) 
match  #o/p:  ['Note 1 – Summary of Significant Accounting Policies']

pattern="Note \d \- [^\n]*"
match=re.findall(pattern, string)
match

pattern="Note \d \- ([^\n]*)"  #which part in() only this part print
match=re.findall(pattern, string)
match  #o/p:  ['Summary of Significant Accounting Policies']

#.................................................................................
import re
string="""The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion."""

#acces the Qutters
pattern="FY\d{4} Q\d"
match=re.findall(pattern, string)
match  #  ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']

pattern="FY\d{4} Q[1234]"   #match the char a,b or c[abc]
match=re.findall(pattern,string)
match  #  ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']

#also give in range 
pattern="FY\d{4} Q[1-4]"  #in range
match=re.findall(pattern, string)
match   #  ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']

#....................................................................................
#if char is a missmatch case FY-fy
import re
string="""The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion."""

pattern="FY\d{4} Q[1-4]"
match=re.findall(pattern, string)
match  #   ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1'] --one is missing


pattern="FY\d{4} Q[1-4]|fy\d{4} Q[1-4]"  #use | (or)   
match=re.findall(pattern, string)
match  #   ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'fy2020 Q4']

pattern="FY\d{4} Q[1-4]"
match=re.findall(pattern, string,re.IGNORECASE)  #re.IGNORECASE---for missmatch
match  #   ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'fy2020 Q4']

pattern="FY(\d{4} Q[1-4])" #used ()--acces without FY
match=re.findall(pattern, string,re.IGNORECASE)  #re.IGNORECASE---for missmatch
match  #   ['2021 Q1', '2020 Q4', '2021 Q1', '2020 Q4']

#acces the cost
pattern="\$[0-9\.]*"  #    *-------acces data upto space
match=re.findall(pattern, string)
match  #   ['$4.85', '$3', '$4.85', '$3']

pattern="\$([0-9\.]*)"  #    *-------acces next string upto space
match=re.findall(pattern, string)
match  #   ['4.85', '3', '4.85', '3']