
"""
a=int(input("Enter the input : "))
    
b=int(input("Enter the input : "))
def addi(): 
    c=a+b
    print(c)
def subt():
    c=a-b
    print(c)
def mult():
    c=a*b
    print(c)
def divi():
    c=a/b
    print(c)
def modu():
    c=a%b
    print(c)
def floo_divi():
    c=a//b
    print(c)
x=int(input("Enter 1 for add, 2 for sub, 3 for mul, 4 for div, 5 for modulus, 6 for floor division :" ))
            
if (x==1):
    
    addi()
elif (x==2):
    subt()
elif (x==3):
    
    mult()
elif (x==4):
    divi()
elif (x==5):
    modu()
elif (x==6):
    floo_divi()
else:
    print("Enter correct value")


#lambda

multi=lambda a,b:a*b
print(multi(5,10))

fun=lambda:print("hola")
fun() 

x=int(input("enter the value: "))
print((lambda x:x**0.5)(x)) 


def fun(x,y):
    return lambda z,n:z+x+y+print(lamb(15,20))
print(lamb(30,60)) """

#reverse
x=int(input("value: "))
temp=x
y=0
while (temp>0):
    n=temp%10
    y=(y*10) + n
    temp=temp//10
    print(y)
    print(temp)


