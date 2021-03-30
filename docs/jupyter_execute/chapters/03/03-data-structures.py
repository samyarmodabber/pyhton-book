# Data structures

## Introduction

**Data type**
* int
* complex
* float
* boolian

**Data structures**

The main data structures in Python divided to two categories: 
* A.	Sequences:
strings, list, tuples

* B.	Non-sequences:
dictionaries, sets

## A. Sequences  (List, tuples, and strings)  have several commonalities:
1. Their length can be queried with the `len` function.
2. Thet are `immutable`.
3. They can be concatenated with the `+ operator`.
4. They repeated with the `* operator`.
5. Since they are `ordered`, we can refer to the elements by integers using the `indexing` notation.

s='A list contains arbitrary number of elements.'

# len(s)
# s[0]='a'
# s+s
# 'Arash '*10
# s[3]
s[-1]

## A.	Sequences: List
A list contains arbitrary number of elements (even zero) that are stored in sequential order. The elements are separated by commas and written between brackets. The elements don’t need to be of the same type. An example of a list with four values:

mylist1=[2, 100, "hello", 1.0]
print(mylist1)
print(id(mylist1))

mylist2=[2, 100, "hello", 1.0]
print(id(mylist2))


# print(mylist1==mylist2)
print(mylist1 is mylist2) # print(id(mylist1() == id(mylist2))

**Indexing and Slicing**

courses=['Calcules','Physics','Computer','Statistic','Algebra']
# print(courses)

# print(courses[2])
# print(courses[-1])

# print(courses[2:4])
# print(courses[2:])
# print(courses[:2])

print(courses[0:4:2])
# print(courses[-1:0:-1])

# print(courses[::2])
print(courses[1:-2])

**Modifying**

courses=['Calcules','Physics','Computer','Statistic','Algebra']
# print(courses)
#Modifying element of a lists
courses[0]='Calcules1'
# print(courses)
# #Modifying any slice of a lists
courses[0:2]=['Calcules1','Calcules2','Physics1','Physics2']
# print(courses)
courses.remove('Calcules2')
courses.remove('Physics2')
# print(courses)
courses.append('Analysis')
# print(courses)
courses.insert(4,'Logic')
# print(courses)
newCourses=['Geometry','ODE','PDE']
courses.extend(newCourses)
# print(courses)
poped=courses.pop(-2) # pop()==pop(-1)
print(courses)
print(poped)

courses=['Calcules','Physics','Computer','Statistic','Algebra']

delete=courses.pop(1)
print(courses)

delete

courses=['Calcules','Physics','Computer','Statistic','Algebra']

# courses.reverse()
# print(courses)

# courses.sort()
# print(courses)

# courses.sort(reverse=True)
# print(courses)

# after_sorted=sorted(courses)
# print(after_sorted)
# print(courses)

# marks=[-5,-4,3,2,6]
# simple_sorted=sorted(marks)
# print(simple_sorted)

abs_sorted=sorted(marks, key=abs)
print(abs_sorted)

scores=[12, 17, 14, 10, 3, 9, 20, 18]
print(min(scores))
print(max(scores))
print(sum(scores))
print(len(scores))

courses=['Calcules1','Physics1','Computer','Statistic','Algebra']

# print(courses.index('Statistic'))
# print('Computer' in courses)

# tostring=' '.join(courses)
# print(tostring)

my_st='A list contains arbitrary number of elements'
words_list=my_st.split(' ')
print(words_list)

**Range Function**

Trivial lists can be tedious to write: [0,1,2,3,4,5,6]. The function range creates numeric ranges automatically. 

* Then end value is not included in the sequence. 
* consumes less memory than the corresponding list. 

This is because in a list all the elements are stored in the memory, whereas the range generates the requested elements only when needed. For example, when the for loop asks for the next element from the range at each iteration, only a single element from the range exists in memory at the same time. This makes a big difference when using large ranges, like range(1000000).

range1=range(7)
# print(type(range1)) # Note that L is not a list!
# print(list(range1))

# range2=range(3,7)
# print(list(range2))

range3=range(0,20,3)
print(list(range3))

list(range1)
int('123')

## A.	Sequences: Tuple

A tuple is fixed length, immutable, and ordered container. Elements of tuple are separated by commas and written between parentheses. Examples of tuples:

singleton=(3,)               # a singleton
pair=(1,3)              # a pair
triple=(1, "hello", 1.0); # a triple
type(singleton)

triple[2]

Note the difference between (3) and (3,). Because the parentheses can also be used to group expressions, the first one defines an integer, but the second one defines a tuple with single element. As we can see, both lists and tuples can contain values of different type.

We can also modify a list by using mutating methods of the list class, namely the methods append, extend, insert, remove, pop, reverse, and sort. 

Note that we cannot perform these modifications on tuples or strings since they are immutable

## B.	Non-Sequences: Sets
A set is a dynamic, unordered container. 

semester1={'Calcules1','Physics','Computer','Statistic'}
semester2={'Calcules2','Computer','Algebra'}

# print(semester1)
# print('Algebra' in semester1)

# print(semester1.intersection(semester2))
# print(semester1.difference(semester2))
# print(semester1.union(semester2))

empty_set=set() # Not {}
type(empty_set)


## B.	Non-Sequences: Dictionaries
A dictionary is a dynamic, unordered container. 

Instead of using integers to access the elements of the container, the dictionary uses **keys** to access the stored values. 

The dictionary can be created by listing the comma separated key-value pairs in braces. Keys and values are separated by a colon. 

A tuple (key,value) is called an **item** of the dictionary.

student1={'name':'Sara', 
          'age':23, 
          'student_id':2020121110, 
          'courses':{'Calcules2','Computer','Algebra'}
         }

student2=dict([
    ('name', 'Danial'), 
    ('age', 22), 
    ('student_id', 2019121002)
]) 

student3=dict(
    name='Arman', 
    age=18, 
    courses=set()
);


print(student1['name'])
print(student1.pop('age'))
print(student1.get('student_id'))

#print(student1['phone']) # Error
print(student1.get('phone'))
print(student1.get('phone','I can Not Found'))

#Add a key-value
student1['phone']='222-2222-2222'
print(student1['phone'])

student2.clear()

student1={'name':'Sara', 
          'age':23, 
          'student_id':2020121110, 
          'courses':{'Calcules2','Computer','Algebra'}
         }
# print(student1)

# student1.update({'age':24,'courses':{'Logic','Linear Algebra'}})
# print(student1)

# del student1['courses']
# print(student1)


# print(len(student1))
# print(student1.keys())
# print(student1.values())
# print(student1.items())

# for key,value in student1.items():
#     print(key,value)

student1.clear()
print(student1)

student4={}
print(student4)
print(type(student4))
