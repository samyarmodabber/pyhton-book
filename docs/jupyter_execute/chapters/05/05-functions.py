# Function

## Define a Function

def hello_func():
    '''Doc string: This function print a string'''
    print('Hello User')
hello_func()

hello_func()

hello_func?

list?

def login_msg(name):
    print(f'Hello {name}, you login now!')


login_msg('Samyar')

login_msg('Arash')

def login_msg(user):
    return f'Hello {user}, you login now!'
    print('Hi')

msg=login_msg('Samyar')
# print(msg)
msg

def user_age(name,age):
    return f'{name} is {age} years old.'


# print(user_age('Parviz',28))

user_age(28,'Parviz')

user_age(age=28,name='Parviz')

user_age(28)

def user_age(name='User name',age=19):
    return f'{name} is {age} years old.'
print(user_age())

user_age('Reza',32)

def user_age(name='User',age=19):
    return f'{name} is {age} years old.'

user_age(age=18)

##  args, kwargs

Pass ARRAY and DICTIONARY as arguments of a function.

def student_courses(*courses):
    print(courses)
student_courses('Calcules1','Algebra1','Logic')

def student_details(**details):
    print(details)
student_details(neme='Parviz',age=28, is_active=True)

def student_info(*courses,**details):
    print(courses)
    print(details)
student_courses('Calcules1','Algebra1','Logic',neme='Parviz',age=28)

def student_info(*courses,**details):
    print(courses)
    print(details)
    
courses=['Calcules1', 'Algebra1', 'Logic']
details={'neme': 'Parviz', 'age': 28}
student_courses(*courses,**details)

## Function in Function

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

operate(inc,3)

def list_courses(courses):
    print('The courses:')
    for course in courses:
        print(course)
        
def student_des(*courses,**details):
    for key,value in details.items():
        print(f'{key}:{value}')
    list_courses(courses)
    
courses=['Calcules1', 'Algebra1', 'Logic']
details={'neme': 'Parviz', 'age': 28}
student_des(*courses,**details)

## Scope (LEGB)
Local, Enclosing, Global, Built-in

x='global x'
def test():
    y='local y'
    #print(y)
    print(x)
test()
#print(y) ##Error

x='global x'
def test():
    x='local x'
    print(x)
test()
print(x) 

x='global x'
def test():
    global x
    x='local x'
    print(x)
test()
print(x) 

def test(z):
    print(z)
test('local z')
#print(z) ##Eror

import builtins
print(dir(builtins))

m=abs(-10)
print(m)

# You can overwrite bult-in functions
def abs(x):
    if x>0:
        return x
    else:
        return 0

m=abs(-10)
print(m)

## Enclosing

x='global x'
def outer():
    #x='outer x'
    def inner():
        #x='inner x'
        print(x)
    inner()

outer()

## Return a Function

def outer():
    message='Hello'
    def inner():
        print(message)
    return inner()

outer()

def outer():
    message='Hello'
    def inner():
        print(message)
    return inner # not Exe

my_func = outer()
my_func()

def outer(message):
    def inner():
        print(message)
    return inner # not Exe

hi_func = outer('Hi')
bye_func= outer('Bye')
hi_func()
bye_func()

## Decorator Function
A decorator takes in a function, adds some functionality and returns it.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")    
pretty = make_pretty(ordinary)
pretty()

@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()

### Example

def divide(a, b):
    return a/b
#divide(2,0)

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)
divide(2,0)

### Multiple decorators can be chained in Python.

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner




@star
@percent
def printer(msg):
    print(msg)
#printer = star(percent(printer)) we should use this if we dont use decorations
printer("Hello")

@percent
@star
def printer(msg):
    print(msg)

printer("Hello")