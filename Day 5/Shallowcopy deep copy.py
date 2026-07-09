#printing stars right inverted triangle 

for i  in range(5,1,-1):
    for  j in range (1,i):
        print("*",end="")
    print("")

#print hollow diagram

for i in range(1,6):
    for j in range(1,6):
        if(i ==1 or i == 5 or j ==1 or j ==  5):
                print("*",end = "")
        else:
                print(" " ,end="")
    print("")

#escape sequence
print("hi\nsantosh")
print("hi\tsantosh")
print("hello\\santosh")
print("hello\'santosh")
print("hello\"santosh")


#functions in string
name = "santosh vid"
print(name.capitalize())
print(name.lower())
print(name.title())
print(name.upper())
print(name.isupper())
print(name.islower())
print(name.isalnum())
print(name.swapcase())
print(name.isdigit())
print(name.split())
print(name.split("-"))
print(name.split(" ",2))


#deep copy and shallow copy 
#copy is a module it has copy and deepcopy as functions
#import copy first ,mainly mutable obj inside mutable obj we can see the difference, int, float, string not possible.
#copy.copy() shallow copy will create outer list seperate memory location, inside it will be same memory ,hence changing one will effect other.
#copy.deepcopy() in deep copy outer list and inner list both seperate memory location is created hence nothing is effected


