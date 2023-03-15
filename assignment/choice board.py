#-------choice borad---------

def again():
    answer=input("do you want anything else:")
    if answer=="y":
        print("ok")
        menu()
    elif answer=="n":
        print("thank you")
    
def mainmenu():
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.modulo")
    print("6.exit")

    choice=int(input("enter the choice"))
    if choice==1:
        addition()
        again
    elif choice==2:
            substraction()
            again
    elif choice==3:
            multiplication()
            again
    elif choice==4:
            division()
            again
    elif choice==5:
            modulo()
            again
    elif choice==6:
            exit
    else:
        print("invalid choice enter 1-6")

def addition():
    a=int(input("enter the number1:"))
    b=int(input("enter the number2:"))
    c=a+b

    print(c)
    
def substraction():
    a=int(input("enter the number1:"))
    b=int(input("enter the number2:"))
    c=a-b

    print(C)

def multiplication():
    a=int(input("enter the number 1:"))
    b=int(input("enter the number 2:"))
    c=a*b
    print(C)
    
def division():
    a=int(input("enter the number 1:"))
    b=int(input("enter the number 2:"))
    c=a/b

    print(c)

def modulo():
    a=int(input("enter the number 1:"))
    b=int(input("enter the number 2:"))
    c=num1%num2


    print("reminder:",result)
    
                
    

    
