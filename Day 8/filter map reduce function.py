# ternary operator in py
#syntax statement1 condition statement2 true then stmt1 comes else stmt2
a  = 10
b  = 20

res = "a is big" if a > b else  "b is big"
print(res)


# sum(), max()  , min() functions on iterable objects

l = [1,2,3,4]

print(sum(l))
print(max(l))
print(min(l))



#filter func - applies defined func to every element in iterable object 
#syntax - filter(func , iterable)

def even(n):
	if (n%2 == 0):
	return	True
	else:
	return False

numbers = {1,2,3,4,5,6,7,8,9,10}

result = filter(even,numbers)
print(list(result)

#what filter does is it runs a loop using even func.

result= []

for i in numbers:
	if even(i) :
		result.append(i)

# When even func return True its appended else discarded.



# lamda func is a anonymous unnamed func contains only one expression
# syntax 
lamda parameter : expression 
parameter = input 
expression = value to return 

numbers = {1,2,3,4,5,6,7,8,9,10}

result =  filter(lambda  n : n%2==0 ,numbers)

print(list(result))


#  filter positive numbers from a given list using filter and lambda

list_1 = [-1,-3,1,4,5,6,0]
result  = filter(lambda n : n > 0,list_1)
print(list(result))

# fitler + nos using filter
list_1 = [-1,-3,1,4,5,6,0]

def positve(n):
    return n > 0 #here return itself gives True or False

result = filter (positve,list_1)
print(list(result))


# print to fitler words with length > 3

list_1 = ["santosh","jagadish","arun","sunny","ab"]

def check(n):
    return len(n) >3

result = filter(check,list_1)
print(list(result))


# print to fitler words with length > 3

list_1 = ["santosh","jagadish","arun","sunny","ab"]
result = filter(lambda n : len(n)>3,list_1)
print(list(result))

# map does operation on list  and give result filter only checks True or False and gives result 
#Unlike filter(), which keeps or discards elements, map() transforms every element.

# map function to square a list and give output

list_1= [1,2,3,4,5,6,7]

def square(n):
    return n**2

result = map(square,list_1)
print(list(result))

#map runs a loop and gives result 
for  item in list_1:
    result.append(square(item))
    

#using lambda function 

list_1= [1,2,3,4,5,6,7]

print(list(map(lambda n : n**2,list_1)))


#reduce function
#reduce() → combines all elements into one final value.
from functools import reduce

list_1 = [1,2,3,4,5,6]
print(reduce(lambda x,y:x*y,list_1))
or 
print(reduce(lambda x,y : x if x > y else y ,list_1))


#using reduce function , finding max 

from functools import reduce

list_1 = [1,2,3,4,5,6,2,1]

def maxi(x,y):
    if x > y:
        return x
    else:
        return y

result = reduce(maxi,list_1)
print(result)


