import math
#function to print the quadratic residues from 0 to the prime number/2

def quadratic_residues(p):
    quadratic_recidue=[]
    k=int((p-1)/2)
    print(k)
    for i in range(0,k+1):
        res=(i*i)%p
        quadratic_recidue.append(res)
    print("quadratic_residues are:-",quadratic_recidue)


#calculating the y square values
def equation(a,b,p):
    y_square=[]
    for i in range(p):
        res=((i*i*i)+a*i+b)%p
        y_square.append(res)
    print("y square values are:-",y_square)


#calculating the lambida value
def flambida(x1,y1,x2,y2,a,p):
    if x1==x2 and y1==y2:
        lambida=((3*(x1*x1)+a)*pow((2*y1),(p-2)))%p
        print("lambida value is",lambida)
    else:
        lambida=((y2-y1)*pow((x2-x1),(p-2)))%p
        print("lambida value is",lambida)
    return lambida


#calculating the x3, y3 points no need lambida value
def points(x1,y1,x2,p,y2,a):
    lambida=flambida(x1,y1,x2,y2,a,p)
    x3=(pow((lambida),2)-(x1+x2))%p
    y3=(lambida*(x1-x3)-y1)%p
    print("(",x3,y3,")")
    return x3,y3

def operation(prefix,x1,y1,x2,p,y2,a):
        for  i in range(prefix-1):
            lambida=flambida(x1,y1,x2,y2,a,p)
            x3=(pow((lambida),2)-(x1+x2))%p
            y3=(lambida*(x1-x3)-y1)%p
            x1=x3
            y1=y3
        print(x3,y3)

def eliptic_curve(a,b,p):
    res=((4*a*a*a)+27*b*b)%p
    if res==0:
        print("curve cant be used")
    else:
        prefix=int(input("please enter the prefix"))
        x1=int(input("enter the value of x1 "))
        y1=int(input("enter the value of y1 "))
        x2=int(input("enter the value of x2 "))
        y2=int(input("enter the value of y2 "))
        operation(prefix,x1,y1,x2,p,y2,a)

print("enter 1 if you wnat to know the quadratic residues ")
print("enter 2 if you wnat to know the y square value ")
print("enter 3 lambida value ")
print("enter 4 to find the points x3,y3 no nned lambida value")
print("enter 5 calculate N(P) where n is the prefix and p is the point")
print("enter 6 if you want to continue with the eliptic curve")

choice=int(input("enter the choice "))
if choice==1:
    p=int(input("enter the primr nukmber until which you want the quadratic resides "))
    quadratic_residues(p)
elif choice==2:
     p=int(input("enter the prime number "))
     a=int(input("enter the value of a "))
     b=int(input("enter the value of b "))
     equation(a,b,p)
elif choice==3:
    x1=int(input("enter the value of x1 "))
    y1=int(input("enter the value of y1 "))
    x2=int(input("enter the value of x2 "))
    y2=int(input("enter the value of y2 "))
    a=int(input("enter the value of a "))
    p=int(input("enter the prime number "))
    flambida(x1,y1,x2,y2,a,p)
elif choice==4:
    x1=int(input("enter the value of x1 "))
    y1=int(input("enter the value of y1 "))
    x2=int(input("enter the value of x2 "))
    y2=int(input("enter the value of y2 "))
    a=int(input("enter the value of a "))
    p=int(input("enter the prime number "))
    points(x1,y1,x2,p,y2,a)
elif choice==5:
    prefix=int(input("please enter the prefix"))
    x1=int(input("enter the value of x1 "))
    y1=int(input("enter the value of y1 "))
    x2=int(input("enter the value of x2 "))
    y2=int(input("enter the value of y2 "))
    a=int(input("enter the value of a "))
    p=int(input("enter the prime number "))
    operation(prefix,x1,y1,x2,p,y2,a)
elif choice==6:
    a=int(input("enter the value of a "))
    b=int(input("enter the value of b "))
    p=int(input("enter the prime number "))
    eliptic_curve(a,b,p)