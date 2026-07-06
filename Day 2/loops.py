#simple if condition
a = 10
b = 5
if(a<b):
    print(f"a is not greater than b")
# nothing prints if condition fails.


# if - else used for single condition
a,b = 10,20

if (b>a):
    print(f"b is greater than a value of a is {a} and value of b is {b}")
else:
    print(f"a is greater than b")

# to check more than one condition
n = 10
if(n > 0):
    print(f"n is greater than zero and its positive and value of n is {n}")
elif(n < 0 ):
    print(f"n is less than zero")
else:
    print(f"n is zero")


# with out using elif we can using if only

n = int(input("enter a number "))

if(n>0):
    print(f"n is positive")
else:
    if(n<0):
        print(f"n is negative")
    else:
        print(f"n is zero")


example 2 :

n = int(input("enter your marks "))

if (n > 90):
    print("you secured grade A")
else:
    if(n > 75):
        print("you secured grade B")
    if(n > 50):
        print("you secured grade C")
    else:
        print("you have failed")
         


# to check given number is even or odd
x = int(input("please give a number "))

if (x%2) == 0:
    print(f"given number is {x} and its even")
else:
    print(f"given number id odd")



# divisibility by any two numbers
x = int(input("give your first number "))
y = int(input("give your second number "))
z = int(input("give number to check"))
if (z%x == 0) and (z%y == 0):
    print(f"given number {z} is divisible by both {x} and {y}")
else:
    print(f"given number is not divisible")


# to check if given char is vowel and consonant using in operator
L = ['a','e','i','o','u']

x = input("give a character ")

if (x in L):
    print(f"given char is vowel")
else:
    print(f"give char is consonant")


n = int(input("give me a number "))
match  n  :
    case 1:
        print("its 1")
    case 2:
        print("its 2")
    case 3:
        print("its 3")
    case _:
        print(f"this is default case and given value is {n}")

#iterative  loops -- while loop -- to print series of numbers
i = 0
while(i < 10):
    print(f"print number in given range {i}")
    i += 1
	


#iterative  loops -- while  -- summing numbers
x = int(input("give a number "))
i = 0
sum = 0
while (i <= x):
    sum += i
    i += 1
print(f"sum of range {x} is {sum}")
	


#iterative  loops -- while -- else   -- summing numbers
#  loop runs and when condition fails else is executed
x = int(input("give a number "))
i = 0
sum = 0
while (i <= x):
    sum += i
    i += 1
else:
    print(f"sum of range {x} is {sum}")


## while - else - break
# when we use break inside while , cursor comes out of else and esle is not executed

x  = int(input("enter a number "))

i = 0
while(i<x):
    if(i == 3):
        break
    print(f"this is iteration number {i}")
    i += 1 
else:
    print("this is else part")
print("this is print statment outside while loop")

#when else is executed it means w/o break its executed


# printing a given table
x = int(input("give a number to print its table "))
i = 0
print(f"table of {x} is ")
while(i <= 10):
    print(f"{x}*{i}=",x*i)
    i+=1


	