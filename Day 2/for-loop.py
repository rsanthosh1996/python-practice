# For Loop 
# Syntax To work at element level in Sequence type using For Loop.

name= 'santosh'
for i in name:
    print(i,end="")

# we use this for list,tuple,string,set


# for dictionary its different
employee = {"employee1":"santosh",
            "employee2":"rupesh",
            "employee3":"chubs",
            "employee4":"neel"}

for i in employee:
    print(i,employee[i])
# here i prints keys only

# to print keys, values, items gives tuple ,key-value using items we use


for i in employee.keys():
    print(i)
for i in employee.values():
    print(i)
for i in employee.items():
    print(i)
for key,value in employee.items():
    print(f"value of {key} is {value}")
 

# print sequence of numbers using for loop
# while requires start , end but for directly we give range

for i in range(6):
    print(i)

# range  specified
for i  in range(1,11):
    print(i)

# using input by user
x = int(input("enter a number"))

for i in range(1,x+1):
    print(i)


## check prime number using for loop

x  = int(input("give me a number "))

for i in range(2,x):
    if(x%i) == 0:
        print("this is not prime number")
        break
else:
    print("this is prime number")


## multiplication of seq of n numbers using for loops

x = int(input("give a number "))
mul = 1
for i in range(1,x+1):
    mul *= i
print(f"multiplied value is {mul}")


## sum of seq of numbers using for loop
x = int(input("enter a number "))
sum = 0
for i in range(1,x+1):
    sum += i
print(f"sum of given series is {sum}")





