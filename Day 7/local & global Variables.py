#we can send list also as argumment , we have used arbitrary *x since our args where multiple comma based.multiple lists also can be send to *x

#sending list as argument to function

list_1 = [10,20,30,40]

def welcome(x):
    for i  in list_1:
        print("welcome",i)

welcome(list_1)


# to restrict only to positional args, we use  ,/
def user(x,y,/):
    print(x,y)

user("santosh","jagadish")


#to restrict to only keyword args *,
def user(*,x,y):
    print(x,y)

user(y="santosh",x="hopeful")

#combine positional and keyword args restrict
#here / means it treats a ,b as positional args ends there. 
def user(a,b,/,*,c,d):
    print(a,d,c,d)

user("santosh","help",c="hope",d="god")


#Global and Local Variables concept
local variables - variables  used inside definition of func . (parameters included), These are accessible inside func only
global variables defined outside func definition . we can use same identifiers  as local variables.These can be used inside func also.

p = 10

def check():
    q =  20
    print(f"p is global variable and value id {p}")
    print(f"q is local variable {q}")

check()


#global variable was hidden inside func when same variable was assigned diff value  

def check():
    p = 20
    print(f"value of p inside func {p}")

p = 10
print(f"value of p before calling func {p}")
check()
print(f"value of p  after calling func {p}")


#  if we want to use global p variable inside func then we have inform inside func
#global p

def check():
    global p
    p = 20
    print(f"value of p inside func {p}")
        
p = 10
print(f"value of p before calling func {p}")
check()
print(f"value of p  after calling func {p}")
