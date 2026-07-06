##summing digits in number using while loop
x = int(input("enter a number "))

sum = 0

while (x>0):
    rem = x%10
    sum += rem
    x = x//10
print(f"sum is {sum}")



#reverse of a number using slicing
x = input("enter a number ")
print(x[len(x)::-1])

# reverse of a number using while loop
x = int(input("enter a number "))

while (x>0):
    rem = x%10
    print(rem,end="")
    x = x//10


# sum of first and last digit number
x =  int(input("enter a number "))
l= x%10
print(f"last digit is {l}")
while(x > 0):
    if(x < 10):
        res= l+x
        print(f"first digit is {x}")
    x = x//10
print(f"sum of first and last digit is {res}")


# to check for palindrome

y = x = int(input("enter a number "))

r = 0


while (x > 0):
    rem = x%10
    r = r*10 + rem
    x=x //10

print(f"give number is {y} and reverse of it is {r}")

if(y==r):
    print("its palindrome")
else:
    print("its not palindrome")


# factorial of a number
x = n = int(input("enter a number "))
fac = 1
while (n>0):
    fac *= n
    n -= 1

print(f"factorial of given  number {x} is {fac}")



