#Functions
#Functions are block of code which are executable
#Function overloading is same function name with different parameters.

def sum():
	a = 2
	b = 1
	print(a+b)
	
sum()


def sum(x,y):
	a  = x
	b  = y
	sum = a+b
	print(sum)
	
sum(1,5)


def sum(x,y):
    sum =  x+y
    print(f"sum of given 2 numbers is {sum}")

a = int(input("give first number "))
b = int(input("give second number "))

sum(a,b)
	
#variables used in functions are confined to that func only , outside u can use same variables again.
#return is  used to return result where function was called hence assign this calling func to a variable

def sum(x,y):
    sum =  x+y
    return sum
a = int(input("give first number "))
b = int(input("give second number "))

d= sum(a,b)
print(f"the sum is {d}")

#more than one value can be  returned only in python
def sum(x,y):
    sum =  x+y
    return x,y,sum
a = int(input("give first number "))
b = int(input("give second number "))

d,f,h = sum(a,b)
print(f"the sum of {d} and {f} is {h}")	

# tuple will be created when returned multiple values stored in single variable
#types of arguments in python - positional arguments, default arguments, keyword args, arbitrary args , keyword arbitrary args

#default args
def address(city,state,country="india"):
	print(city,state,country)
	
address(hyd,telangana)
address(ohio,chicago,america) = here it replaces default value

#keyword args
def big(x,y):
	if(x>y):
		print("x is greater")
	else:
		print("y  is greater")
		


big(y=20,x=10)

or 
big(y = int(input("enter a args"),x = int(input("enter another arg")))

#arbitrary args
def users(*x):
    print("welcome",x)

users("santosh",123)
users("nallabalu","salmon","koko")


#individual welcome
# here it takes only positional arguments if i give x = "santosh" it ll throw type error
def users(*x):
    for i in x:
        print("welcome",i)

users("santosh",123)
users("nallabalu","salmon","koko")

#arbitrary keyvalue args
# we give multiple arguments and assign it to a keyword 
# These are converted into dictionary since we give in key value pairs

def users(**x):
    for k,v in x.items():
        print("welcome",k,v)

users(name = "santosh",age = 29)



