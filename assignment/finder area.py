# finder area

#print("--------finder area-------")

def mainmenu():
    print("1.circle")
    print("2.rectangle")
    print("3.triangle")
    if find==1:
        circle()
    elif find==2:
        rectangle()
    elif find==3:
        triangle()
    else:
        print("enter the choice1-3")
        mainmenu()

def circle():
    r=int(input("enter radius of circle:"))
    pi=3.14
    area=pi*r*r
    print("area given of circle:",area)

def rectangle():
    l=int(input("enter the length of rectangle:"))
    b=int(input("enter the base of rectangle:"))
    area=l*b
    print("area given of rectangle:")

def triangle():
    h=int(input("enter the hieght of triangle:"))
    b=int(input("enter the base of triangle:"))
    area=(0.5)*h*b
    print("area given of triangle:")
    
