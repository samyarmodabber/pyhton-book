# Basic and String

## Basic

**Hello World!**

#Print Hello 
print('Hello world')

#Case sensetive
# Print('Hello world')


**input**

name=input("Give me your name: ")
print("Hello,", name)

**variable**

message='Hello world!'
# print(message)
# type(message)
# len(message)

a=b=c='Hello'
print(a,b,c)

first_name='Sara'

#Wrong syntax
# first-name ='Sara'
# 5_name ='Sara'
# first name ='Sara'

**Single qoutes and duble qoutes**

message1="He's my friend."

message2='His name is "Milad".'
#  He's "Milad"
message3='He\'s an "Artist".\n New line'

print(message1)
print(message2)
print(message3)


**Multi line**

message4="""Hello Milad
I am intereted to learn Python.
Could you teach me?
Sincerely,
Sohrab
"""
print(message4)

**Indexing and Slicing**

message5='Hi. Where are you nowdays?'

## one element
print(message5[0])


# Interval
print(message5[0:4])
print(message5[:4])
print(message5[4:])
print(message5[19:25])
print(message5[0:25:2])

## Negetive
print(message5[-1])
print(message5[-7])

print(message5[8:-7])
print(message5[-2:2:-1])
print(message5[::-1])

**lower, UPPER**

message6='thanks dear Saam.'
print(message6.lower())
print(message6.upper())
print(message6.capitalize())

print(message6.count('s'))
print(message6.count('aa'))

print(message6.find('Saam'))
print(message6.find('Sam'))

**replace**

message7='I am intereted to learn Python.'
edited=message7.replace('e','_')
print(edited)

print(message7)

message7=message7.replace('e','_')
print(message7)

message7='I am intereted to learn Python.'
edited=message7.replace('e','_',2)
print(edited)

**concat**

name='Ramin'
welcome='Welcome, dear'

message8=welcome+ ' ' + name+'!'
print(message8)

**format and f**

name='Armin'
unread_messages=23

print('Dear {}, you have {} unreaded message(s).'.format(name,unread_messages))

print(f'Dear {name}, you have {unread_messages} unreaded message(s).') #python 3.6+

print(f'Dear {name.upper()}, you have {unread_messages:3d} unreaded message(s).') #python 3.6+


**dir and help**

message10='bye'

# print(dir(message10))
# print(help(str))
print(help(str.find))

## Methods

In Python strings are **immutable**. This means that for instance the following assignment is not legal:

``s="text"
s[0] = "a"    # This is not legal in Python
``

Because of the immutability of the strings, the string methods work by returning a value; they don’t have any side-effects. 

In the rest of this section we briefly describe several of these methods. The methods are here divided into five groups.


**1.	Classification of strings:**

All the following methods will take no parameters and return a truth value. An empty string will always result in False.


s=' All the following Methods.'

# s.isalpha() #True if all characters are letters
# s.isdigit() #True if all characters are digits
# s.isalnum() #True if all characters are letters or digits

# s.islower() #True if contains letters, and all are lowercase
# s.isupper() #True if contains letters, and all are uppercase
#s.isspace() #True if all characters are whitespace
#s.istitle() #True if uppercase in the beginning of word, elsewhere lowercase

**2.	String transformations:**

The following methods do conversions between lower and uppercase characters in the string. All these methods return a new string.


s=' All the following Methods.'
print('main srting:',s)

sl=s.lower() #Change all letters to lowercase
print('lower:',sl)

su=s.upper() #Change all letters to uppercase
print('upper:',su)

sc=s.capitalize() #Change all letters to capitalcase
print('capitalize:',sc)

st=s.title() #Change to titlecase
print('title:',st)

ss=s.swapcase() #Change all uppercase letters to lowercase, and vice versa
print('swapcase:',ss)


**3.	Searching for substrings:**

All the following methods get the wanted substring as the parameter, except the replace method, which also gets the replacing string as a parameter

s=' All the following methods'
substr='ll'
m=s.count(substr) #Counts the number of occurences of a substring
print(f'sc:{m}')

sf=s.find(substr) #Finds index of the first occurence of a substring, or -1
sr=s.rfind(substr) #Finds index of the last occurence of a substring, or -1
print(f'sf:{sf} sr:{sr}')

##ValueError
si=s.index(substr) #Like find, except ValueError is raised if not found
sri=s.rindex(substr) #Like rfind, except ValueError is raised if not found
print(f'si:{si} sri:{sri}')

target='All'
start=s.startswith(target) #Returns True if string starts with a given substring
end=s.endswith(target) #Returns True if string ends with a given substring
print(f'start:{start} end:{end}')

replacement='-'
sn=s.replace(substr, replacement) #Returns a string where occurences of one string are replaced by another
print(f'sn:{sn}')

**4.	Trimming and adjusting**

s='  Removes   leading and   '
x='s'
s.strip() #Removes leading and trailing whitespace by default, or characters found in string x
#s.lstrip(x) #Same as strip but only leading characters are removed
#s.rstrip(x) #Same as strip but only trailing characters are removed
n=20
#s.ljust(n) #Left justifies string inside a field of length n
#s.rjust(n) #Right justifies string inside a field of length n
s.center(n) #Centers string inside a field of length n

**5.	Joining and splitting:**

The join(seq) method joins the strings of the sequence seq. The string itself is used as a delimitter. An example:

allStr="*".join(["abc", "def", "ghi"])
print(allStr)

s='method joins the strings of the sequence'
sp=s.split()
print(sp)