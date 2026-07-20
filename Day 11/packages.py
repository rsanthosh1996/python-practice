#recursion modules and functions
#function calling it self is called  recursion
def add(x,y,z):
    return x+y+z

def avg(a,b,c):
    s = add(a,b,c)
    average = s//3
    return average

def avg50(e,f,g):
    d=avg(e,f,g)
    if d > 50:
        print("avg is  > 50")
    else:
        print("avg is !> 50")

avg50(1,2,300)


#return can be used to come out of function.

def check(n):
	print("hi",n)
	n +=1
	if(n==100):
		return
	check(n)
	
check(10)


#  factorial using  recursion functions
mul = 1
def check(n):
    global mul
    mul *= n
    n -= 1
    if (n==1):
        print(f"factorial of n is {mul}")
        return
    check(n)


check(5)

#instead of loop we can use recursion functions
#os module and use elements mkdir,chdir,listdir,rmdir
#random module to generate random numbers
#__pycache__  file is created when a module is used inside another module for that  used module only
# if module is outside folder then create it as package to use it.__init__.py create one empty to make the folder package.
# also add package path where we are using it ,using sys module 

# example of package 
def patient():
	name ="santosh"
	age = 29
	return name,age


import sys
sys.path.append(r"C:\\Users\\SantoshVid\\Desktop\\patient")

import patient as p

name,age = p.patient()
print(f"give some  medicines to {name}")
