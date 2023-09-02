'''def outer_fun():
    print("hello,brother!")
    def inner_fun():
        print("shall,we?")
    return inner_fun() 
outer_fun()

#nested concept
def outer_fun():
    a=5
    def inner_fun():
        b=10
        return( a+b)
    inner_fun()
print(outer_fun)


#closure concept
def outer_fun(x):
    a=5
    def inner_fun(y):
        b=10
        return a+b+x+y
    return inner_fun
answer=outer_fun(50)
print(answer(100))

def outer(x):
    a=5
    def inner(y):
        b=10
        return a+b+x+y
    return inner
ans=outer(2)
ans1=outer(5)
print(ans1(ans(1))) 


def decor(fun):
    a=10
    def ifun():
        b=5
        fun()
        return (a+b)   
    return ifun
@decor
def ofun():
    print("mystic falls")
print(ofun()) 

def decor(fun):
   
    def ifun():
        print("hello")
        fun()
        print("how are you")
    return ifun

def cfun(x):
    a=5
    def inner_fun(y):
        b=25
        return (a+b+x+y)
       
    return inner_fun
@decor
def res():
    def rev():
        yval = cfun(50)
        print(yval(50))
        
        
    return rev()
res() 
#tuesday(25/7/23)

list_01="Hello"
iter_01=iter(list_01)
print(next(iter_01))
print(next(iter_01))
print(iter_01.__next__())
print(next(iter_01))
print(next(iter_01))
print(next(iter_01))   


#map function()
num=(1,2,3,4)
num2=(1,2,3,4)
result=map(lambda x,y :x*y,num2,num)
print(set(result)) 
#exponent sum
num=(1,2,3,4) 
result=map(lambda n :n*n,num)
print(list(result))
#thursday(27/7/23)
lst=[]
print(type(lst))
print(dir(lst))

string=" "
print(type(string))
print(dir(string))


class chennai:
    name="siva"
    age="6"
    def mall(self):
        print("Marina mall")
    def beach(self):
        print("marina beach")
    
person_01=chennai()
person_02=chennai() 
class chennai:
    x=10
place=chennai()
print(place.x) 

#class
class Pencil:
    name="siva"
    age="6"
    def fun(self):
        print(self.name,"your age is", self.age)
obj=Pencil()
obj.fun()
obj.name="kavi"
obj.age="45"
obj.fun()
obj_01=Pencil()
obj_01.name="nila"
obj_01.age="20"
obj_01.fun() 

#constructor
class Pencil():
    x="alarie"
    print(x)
    #print(x)
    def __init__(self):
        y="zoe"
        print(y)
    def fun(self):
        z="maddy"
        print(z)
obj=Pencil()
obj.fun() 

class Laptop:
    def __init__(self):
        self.ram=" "
        self.processor="  "
    def display(self):
        print("ram: ",self.ram)
        print("processor: ",self.processor)
hp=Laptop()
dell=Laptop()

hp.ram="8gb"
hp.processor="i5"
dell.ram="16gb"
dell.processor="i7"

hp.display()
dell.display() 
#28/7/23(friday)
#instance variable eg:
class Laptop:
    def __init__(self,brand,price,processor):
        self.brand=brand
        self.price=price
        self.processor=processor
    def menu(self):
        print("brand: ",self.brand)
        print("price: ",self.price)
        print("processor: ",self.processor)
model_1=Laptop("Dell","50,000","i5")
model_1.menu() 
model_2=Laptop("hp","75,000","i7")
model_2.menu() 

#class variable:
class Laptop:
    processor="i7"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def menu(self):
        print("brand: ",self.brand)
        print("price: ",self.price)
        print("processor: ",self.processor)
model_1=Laptop("Dell",50000)
model_1.menu()
Laptop.processor="i5"
model_2=Laptop("hp","75,000")
model_2.menu()


#class method
class MyClass:
    class_variable=0
    def __init__(self,value):
        self.value=value
    @classmethod
    def increment_class_variable(cls,num):
        cls.class_variable=cls.class_variable+num
obj1=MyClass(10)
obj2=MyClass(20)
MyClass.increment_class_variable(5)
print(MyClass.class_variable) 



class MyClass:
    @staticmethod
    def add_numbers(x,y):
        return x + y
result=MyClass()
print(result.add_numbers(3,5))

def name(*lname):
    print("hello",lname)
name("mani" ,"sam")

def name(**fname):
    print("hello",fname["key1"])
name(key1="dog",key2="cat") 

#inheritance constructor (super function):
class Section():
    def __init__(self):
        
        print("hello")
class name(Section):
    def __init__(self):        
        print("good morning")
class age(name,Section):
    def __init__(self):
        super().__init__()
        print("20")
class percent(age):
    def __init__(self):
        super().__init__()
        print("20%")
obj_3=percent() 


class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(self.name)
        print(self.age)
class B:
    def year(self,year): #without the construtor
        self.year=year
        print(self.year)
obj_1=A("john","25")
obj_1.details()
obj_2=B()
obj_2.year("2023") 


class Car:
    def break_1(self):
        print("break")
    def wheel(self):
        print("Four wheeler")
class Bike(Car):
    def wheel(self): 
        print("two wheeler")
obj_1=Car()
obj_1.break_1()
obj_1.wheel()
obj_2=Bike()
obj_2.break_1()
obj_2.wheel() 

class Father():
    def __init__(self,name):
        self.name=name
        print(self.name)
class Son(Father):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
     def display(self):
        print(self.name)
        print(self.grade)
s1=Son("Alex","A")
s1.display()
f1=Father("dada") 

#7/8/2023 (over riding)
class One:
    def details(self):
        print("hello to user" )
class Two(One):
    def details(self):
        print("Hello to new user")
obj_1=One()
obj_2=Two()
obj_1.details()
obj_2.details() 

class First:
    def rank(self):
        print("shakthi")
class Two(First):
    def rank(self):
        super().rank()
        print("mohan")
class Third(Two):
    def rank(self):
        
        print("mani")
        super().rank()
obj=Third()
obj.rank() 

#private --- double underscore
class Bank:
    def __person_3(self):
        print("Name : Sona")
        print("Age : 25")
class Xent(Bank):
    def hell(self):
        super().person_3()
        pass
9obj_1=Bank()
obj_1._Bank__person_3()
#print(dir(obj_1)) 


#protected -- single underscore
class Bank:
    def _person_3(self):
        print("Name : Sona")
        print("Age : 25")
class Xent(Bank):
    def hell(self):
        super().person_3()
        pass
obj_1=Bank()
obj_1._person_3()
print(dir(obj_1)) 

#8/8/23(tuesday)
#abstraction
from abc import ABC,abstractmethod
class Shapes(ABC):
    @abstractmethod
    def pent(self):
        print("four sides")
    
    def hex(self):
        print("six sides")
class Shape(Shapes):
    def pent(self):
        print("i have a five sides")
    def pen(self):
        print("i have five sides")
class Shap(Shapes):
    def pent(self):
          print("i too have five sides")
obj_1=Shape()
obj_1.pen()
obj_2=Shap()
obj_2.pent()
obj_2.hex() 

class Car:
    def __init__(self,make,model):
        self.make=make
        self._model=model
        self.__mileage=0
    def drive(self,miles):
        self.__mileage += miles
    def get_mileage(self):
        return self.__mileage
class Bike(Car):
    def cc(self):
        print(self._Car__mileage)
my_car=Car("tata","BYD")
my_car.drive(100)
print("Mileage:",my_car.get_mileage())
obj=Bike("RR","Von")
obj.cc()


#9/8/23(wednesday)
class Cls:
    def __init__(self,x=0):
        self._x=x
    def get_x(self):
        return self._x
    def set_x(self,y):
        self._x=y
obj=Cls(2)
obj.set_x(10)
print(obj.get_x())
print(oimport requests
x=requests.get("https://www.w3schools.com")
print(x.get)
bj._x) 



#16/8/23(wednesday)
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
print(x.strftime("%A"))    
print(x.strftime("%a"))  '''

#17/8/23(thu)
import requests
x=requests.get("https://www.w3schools.com")
print(x.text)



