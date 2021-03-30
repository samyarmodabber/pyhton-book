# Conditions and Loops

## if, elif, else

# a='sara' #23
# b='saara' #22
a =[2,3,5,8]
b= [2,3,7]

if a==b:
    print(f'{a} is equal {b}.')
elif a>b:
    print(f'{a} is greater than {b}.')
elif a<b:     
    print(f'{a} is less than {b}.')
else:
    print('Non of theme')

### Logic operators

user='Admin'
logged_in=False

if user=='Admin' and logged_in:
    print ('Admin Page')
elif not logged_in:
    print('Login Page')

### False Value
* False
* None
* Zero
* Empty structure: '',  [],  (), {} 

if None or 0 or [] or () or {} or '':
    print('One of them is True')
else:
    print('All of them are False')

## For

courses=['Calcules','Physics','Computer','Statistic','Algebra']

for c in courses:
    print(c)

courses=['Calcules','Physics','Computer','Statistic','Algebra']

for _ in courses:
    print('*')

list(range(7))

for i in range(7):
    if i%2==0:
        print(f'{i} is Even.')
    else:
        print(f'{i} is Odd.')

limit=3

for i in range(1,7):
    if i<limit:
        print(f'Your password is not correct. {i}/{limit}.')
    else:
        print(f'You input incorrected password {i} times. Your card is blocked.')
        break

for i in range(20):
    if i%3==0:
        continue
    print(i)

for i in range(3):
    for j in 'abc':
        print(i,j)

## while

x = 0

while x<=10:
    x+=1
    print(x)
    

x

u=[2 ,3,6,8,5]
v=[-1,5,0,6,7]

s=0
n=len(u)

for i in range(n):
    s+=u[i]*v[i]
    
s

u=[2 ,3,6,8,5,4,2,5,2]
v=[-1,5,0,6,7,-1,8,6,5]

s=0
n=len(u)

if len(u)!=len(v):
    print(f'dim is not equal: {len(u)} , {len(v)}')
else:
    for i in range(n):
        s+=u[i]*v[i]
    
s

u=[2 ,3,6,8,5,4,2,5,2]
v=[-1,5,0,6,7,-1,8,6,5]

s=0
n=len(u)

if len(u)==len(v):
    for i in range(n):
        s+=u[i]*v[i]
else:
    print(f'dim is not equal: {len(u)} , {len(v)}')
    
    
s

def inner_product(a,b):
    m=len(a)
    n=len(b)
    s=0
    if m==n :
        for i in range(m):
            s+=a[i]*b[i]
    else:
        return 'Dimentions are not equal'
    return s

inner_product(u,v)

u1=[2,3,6]
u2=[0,5,9]
inner_product(u1,u2)

u1=[2,3,6,3]
u2=[0,5,9]
inner_product(u1,u2)

a=[1,2,3,4,5,6,7,8,9]


# 1 2 3
# 4 5 6
# 7 8 9



list(range(1,26))