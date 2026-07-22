def menu():
    marks = {}
    while(True):
        print("menu is \n""1.enter marks\n""2.display marks\n""3.specific marks of a student\n""4.delete marks of a student\n""5.exit\n")
        c = int(input("please enter your option from above menu: "))
        match  c:
            case 1:
                print("marks entry")
                try:
                    rno = int(input("enter roll number"))#valueerror
                    m = float(input("enter marks"))#valueerror
                    marks.update({rno: m})
                except:
                    print("give integer only")
                print("---------- marks entered successfully ------------")
            case 2:
                print("displaying marks")
                for k,v in marks.items():
                    print(f"marks of roll number {k} is {v}")
                print("----- displayed marks successfully--------")
            case 3:
                try:
                    x = int(input("enter student roll number to check marks"))#valueerror
                except:
                    print("give int only")
                try:
                    print(f"marks of given roll number {x} is {marks[x]}")#KeyError
                except:
                    print("give correct key  value")
                print("----------- marks shown successfully of a student-------")
            case 4:
                d =int(input("we are deleting marks of a student give roll number"))
                marks.pop(d)
            case 5:
                print("exiting app")
                break

menu()