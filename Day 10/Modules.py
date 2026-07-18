
#Read a global variable: just use it inside the function. No global keyword is needed.

#Modify a global variable: write global p before using or assigning p inside the function.

#Do not assign before declaring global: p = 30 before global p causes a SyntaxError.

p =10
def check():
    print(p)
check()
print(p)

p = 10
def check():
    global p
    p = 20
    print(p)
print(p)
check()
print(p)

#modules - A  module is a file that contains global variables , funcs and classes
# To reuse variables and funcs from one file to another files.

#import modulename - imports complete module, but need to call by module name.
#To call multiple modules we can give import module1,module2 give alias to reduce burden in code 

#What is the danger of from module import *?” The answer is namespace collision / accidental overwriting of names, exactly what happened here.

#here both batch1 and batch2 have same func name so py goes in order and over writes other previus one.
from batch1 import *
from batch2 import *

x = add(10,40)

print(x)

#module should not have independent line of code it should have func,classes, variables. so when func is called its executed.
#limitation is all module files must be under one file. Packages can be used in the other case.