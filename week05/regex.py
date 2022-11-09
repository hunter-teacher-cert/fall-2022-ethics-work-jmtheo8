# FILENAME: Regex
# First Last: Jerusha Theobald
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 


import re

# Practice Exmples worked out:
# Regular expression (regex), the standared for parsing text in python
# It is good for debugging code
# Scraping the web
# Verifing user input
# e Code built in colab


# re is a regex packgae in python
#import re

#example_string =""" Math, philosophy, computer science and sometimes language 
#all try to deliver a complete representation of the world. that may lead to 
#better understandings and the exposure of inconsistencies and gaps. 
#In order to complete the picture, problem may be approached from two sides: 
#A) From one side we expand our knowledge. B)From the other we work on breaking 
#the mysteries down to little digestible bits  to match with inferred and apporved 
#axioms. Logic is a discipline. Sometimes logical problems need to be approached 
#from both sides. Logic is relevant.  With logic we can find modes of agreement. 
#We can find out if something is true or false, right or wrong. It’s a cognitive 
#science that is branching into math, philosophy, language. It is also a solid 
#basis for accumulating knowledge in the natural sciences. Step 2. One of the 
#essential tools in propositional logic is the connection of two arguments into 
#a complex one. A computer does exactly that and uses electricity to accelerate 
#and automate the process. A computer can let us observe logic in action. 
#It allows us to see if ideas about the world match how the world actually works. 
#The number of questions that can be asked and worlds that can be created and 
#observed is extremely high. Logic is expressed and communicated through 
language. -Source: http://www.cs4fn.org/poems/shapingpoems.php
"""

#finditer is a method that gives a match object works like search() and findall() using a pattern or words and gives the index location
#pattern = re.compile(r"computer")
#matches = text.finditer(example_string)

#for match in matches:
#    print(match)

#Using the findall method to prints all the matches found in the example string
#pattern = re.compile(r"computer")
#matches = text.findall(example_string)
#for match in matches:
#print(matches)


#Using the findall method to prints one beginning and end index of teh first match found in the example string
#pattern = re.compile(r"computer")
#match = text.search(example_string)
#for match in matches:
#print(match)

#To get the match span of the start and stop indexes as a tuple of all matches in the example string
#pattern = re.compile(r"computer")
#matches = text.finditer(example_string)
#for match in matches:
#  print(match.span())

#To get the match span of the beginning of a block with the start and end indexes
#text = re.compile(r'\bscience')
#matches = text.finditer(example_string)
#for match in matches:
#  print(match)

#Replace all white-space characters with a -
#pattern = re.sub("\s", "-", example_string)
#print(pattern)

#Search that will return a match for the word "the" with the start and end idexes
#pattern = re.search("the", example_string)
#print(pattern)

#Search that will return a match for the first uppercase "P" character wrod
#pattern = re.search(r"\bP\w+", example_string)
#print(pattern.group())

#Search that will return a match for the first lowercase "l" character word
#pattern = re.search(r"\bl\w+", example_string)
#print(pattern.group())

#Search that will return a match for specified dates with start and end indexes

dates ="""
#09.12.2022
#12.09.2022
#12.02.2022
#02.12.2022

#2022.12.02
#2022.02.12
#2022.09.12
#2022.12.09

#12-02-2022
#02-12.2022

#10/02/2022
#02/10/2022
"""
#Look for patteres of "four", "two" and "two" digits separated by a '.'
#pattern = re.compile(r'\d\d\d\d.\d\d.\d\d')
#matches = pattern.finditer(dates)
#for match in matches:
#  print(match)

name_string ="""

Ms. Liam
Ms Noah
Mr Elijah
Mr. James
Mrs. Sophia 
Dr.	Lucas	

"""
#Using an optional qualtifier to locate a name by Mr. and Ms. with index
#pattern = re.compile(r'(Mr|Ms)\.\s\w*')
#matches = pattern.finditer(name_string)
#for match in matches:
#  print(match)

email_string = """

jan@gmail.com
feb@gmail.com

mar03@month.org
apr04@month.org

"""
#Grouping in match
pattern = re.compile(r'([a-zA-Z0-9-]*)@([a-zA-Z-]*)\.([a-zA-Z]*)')
matches = pattern.finditer(email_string)
for match in matches:
  print(match.group(0))
  print(match.group(1))
