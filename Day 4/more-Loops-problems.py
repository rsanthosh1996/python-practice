# printing numbers into words
x  = str(int(input("enter a number ")))
w = {"0":"zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five"}

for i in x:
    print(w[i],end="")


# exponent w/o using  operator **
#print value of 2^6

base_1=base = int(input("give me a base number"))
exponent = int(input("give me a exponent number"))

for i in range(1,exponent+1):
    base *= 2
print(f"exponent value of base {base_1} and exponent {exponent} is {base}")


#finding factors of given number using for loop

n = int(input("give me a number to find its factors "))

for i in range(1,n+1):
    if (n%i) == 0:
        print(f" {i}",end="")


#finding factors of  given number using while loop

n = int(input("give me a number to find its factors "))

i = 1
while(i<=n):
    if(n%i) == 0:
        print(i,end=" ")
    i += 1


# printing fibonnaci series  below 100 using while loop

a = 0
b = 1

while(a<100):
    print(a,end = " ")
    a,b = b ,a+b
	


#nested loops for loop printing *
for i in range(1,6):
    for  j in range(1,6):
        print("*",end = "")
    print()


##print prime numbers between 10 to 100
for i in range(10,101):
    for j in range(2,i):
        if(i%j) == 0:
            print(f"{i} is not prime number")
            break
    else:
        print(f"{i} is prime number")


# print stars right triangle as per rows
for i in range(1,10):
    for j in range(1,i+1):
        print("*",end = "")
    print()

