import re
def standard_format(match):
    g1,g2,g3 = match.groups()
    if len(g1) == 4:      
        year = g1
        month = g2.zfill(2)
        day = g3.zfill(2)
    else:                
        month = g1.zfill(2)
        day = g2.zfill(2)
        year = g3
    return f"{year}-{month}-{day}"
def strength_check(password):
    regex=[r'.{8,}',r'[a-zA-Z]',r'\d+',r'[^a-zA-Z0-9]']
    for p in regex:
        if not re.search(p,password):
            return False
    return True
#PRACTICE QUESTION
'''text = "I love Python programming"
pattern = r"Python"

if re.search(pattern, text):
    print("Found!")
else:
    print("Not Found!")'''

# QUESTION-1
#In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
pattern1= r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
paragraph1="""Alice Johnson called Bob yesterday from 415-555-1234 and also shared an alternate number 212-999-8888. 
She asked him to visit https://www.example.com or http://testsite.org for more details. 
Bob replied from bob.smith@gmail.com on 3/14/2015 and later again on 2015/3/14. 
Carol Nakamoto bought a laptop for 1,234 dollars and a phone for 6,368,745 rupees. 
Their old office number was 555-123-4567, but now it is 999-888-7777.
"""
flag=False
matches=re.finditer(pattern1,paragraph1)
for i in matches:
    flag=True
    print("group(0)",i.group(0))
    print("group(1)",i.group(1))
    print("group(2)",i.group(2))
    print("----------")
if not flag:
    print("Required pattern is not found in the given string")

# QUESTION-2
#Find website URLs that begin with http:// or https://.
pattern2=r'(https?://\S+)'
paragraph2="""
Alice was researching cloud platforms and first visited https://aws.amazon.com to learn about EC2 services. 
Later, she checked http://azure.microsoft.com for comparison and bookmarked https://cloud.google.com as well. 
During her research, Bob suggested reading tutorials from https://www.w3schools.com and http://geeksforgeeks.org. 
Carol shared a blog link https://medium.com/@carolwrites about DevOps tools. 
Some invalid links like ftp://fileserver.com and www.fakeurl.com should not be matched. 
Finally, Alice opened https://openai.com and http://example.org before closing her browser.
"""
flag=False
matches=re.findall(pattern2,paragraph2)
for i in matches:
    flag=True
    print(i)
if not flag:
    print("URLs that begin with http:// or https:// are not found in the given paragraph")
print("----------")

# QUESTION-3
#Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14) by 
#replacing them with dates in a single, standard format.
pattern3=r'(\d{1,4})[/-](\d{1,2})[/-](\d{1,4})'
paragraph3="""
Alice was born on 3/14/2002 and her brother was born on 12-05-1999. 
Bob joined the company on 2018/7/1 and got promoted on 01/08/2022. 
Carol’s wedding date is 5-9-2020 and the reception is on 2020/5/10. 
The project started on 03-01-2023 and ended on 2023/3/15. 
David noted his appointment as 9/4/2021 and follow-up as 2021/10/2. 
Emma wrote her exam on 11-11-2024 and result was declared on 2024/11/30.
"""
result = re.sub(pattern3,standard_format,paragraph3)
print(result)
print("----------")

# QUESTION-4
#How would you write a regex that matches a number with commas for every three digits?
pattern4 = r'^\d{1,3}(,\d{3})*$'
num=str(input("Enter a number :"))
if re.match(pattern4,num):
    print(num, "-> Valid")
else:
    print(num, "-> Invalid")
print("----------")

# QUESTION -5
# full name checking
pattern5=r'[A-Z][a-zA-Z]+\sNakamoto$'
tests=["Satoshi Nakamoto",
"Alice Nakamoto",
"RoboCop Nakamoto",
"satoshi Nakamoto",
"Mr. Nakamoto",
"Nakamoto",
"Satoshi nakamoto"
]
for test in tests:
    if re.match(pattern5, test):
        print(test,"-> Match")
    else:
        print(test,"-> No match")
string=input("Try your own string :")
if re.match(pattern5,string):
    print(string,"-> Match")
else:
    print(string,"-> No match")
print("----------")

# QUESTION-6
pattern6=r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$'
string=input("Enter a string:")
if re.match(pattern6,string, re.IGNORECASE):
    print(string, "-> Match")
else:
    print(string, "-> No match")
print("----------")

# Question-7
# PASSWORD CHECKING
password=input("enter a passoword to check its strongness:")
if strength_check(password):
    print("strong")
else:
    print("weak")
