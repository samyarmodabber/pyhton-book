# Integers and Float

## Numbers

**types**

num1=19
num2=3.14
num3=2+3j
print(type(num1))
print(type(num2))
print(type(num3))

**basic operators**

num1=19
num2=7


print('Addition:',num1+num2)
print('Subtraction:',num1-num2)

print('Multiplication:',num1*num2)
print('Exponent:',num1**num2)

print('Division:',num1/num2)
print('Floor Division:',num1//num2)
print('Modulus:',num1%num2)


type(num1)

num=19
# num=num%2

num-=2 ## It can be + - * / % num=num%2
print(num)

num1=-3
print(abs(num1))

num2=3.14
print(int(num2))

num3=16
print(num3**(1/2))


num1=19.19
print(round(num1))
num1=19.99
print(round(num1))

num1=19.19
print(round(num1,1))
num1=19.99
print(round(num1,1))

num1=-19.19
print(round(num1))
num1=-19.99
print(round(num1))



## Logic

p=True
q=False

print(p and q)
print(p or q)
print(not q)

print(p is True)
print(q is not True)

print(None is False)
print(0 is False)

type(print)

## Compare numbers

num1=19
num2=7

print(f'{num1} is equal {num2}?', num1==num2)
print(f'{num1} is not equal {num2}?', num1!=num2)

print(f'{num1} is greater than {num2}?', num1>num2)
print(f'{num1} is less than {num2}?', num1<num2)

print(f'{num1} is greater than or equal {num2}?', num1>=num2)
print(f'{num1} is less than or equal {num2}?', num1<=num2)

result= num1==num3
print('Result:',result)

not num1!=num2

## Convert

print(int(-2.8))
print(float(2))
print(int("123"))
print(bool(-2), bool(0))  # Zero is interpreted as False
print(str(234))

num1='19'
num2='7'

# print(num1+num2)

print(int(num1)+int(num2))



True or True and False #  == True or (True and False)

(True or True) and False



not False and False # == (not False) and True

not (False and False)