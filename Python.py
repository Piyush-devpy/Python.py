#Lesson 1
# Comments -Use for describing your code,writing a note  or write a line that is ignore by python. (#) used for comments.
character_name="Piyush" #This is a variable [Piyush = String]
character_age= "18" #This is another variable[18 = Float]
print("My name is :", character_name)
print("My age is",character_age)
print(character_name.index("y"))#This[index] is used for getting position of the character.
#Index starts from 0 to infinite.
print(character_age.replace("18","19"))#Replace is used for replacing an character (replace("old","new")).
#Replace only works for string.
print(10%3)#We can add(0),subtract(-),multiply(*),divide(/) and get moduler(remainder[%]) in python.
Num=20#This is a Integer.
print(type(str(type(Num))))#This is a string,the integer is converted into string.
print(abs(Num))#This will give absolute value of the number.
print(pow(3,2))#This is used for giving power to the number.
print(max(6,7))#This will print the maximum number.
print(min(-1,0))#This will print the minimum number.
print(round(3.2))#Use for rounding off,ceil works the same,where as floor will grab the smallest number.(from math module)
from math import * #import- used for importing external module,(*) used for importing everything from that module.
print(sqrt(49))#Give the square of the number ,part of math module.
#input() #Use to get input from the user.
Age = int(input("Enter Your Age:"))#user enter his age. example: 18
print("so your age is:",Age)# so your age is :18

#Lesson 2
Name =["Piyush","Jatin","Amit","Vikash"] #List
Number = [1,2,3,4,4]
print(Name)# Output-["Piyush","Jatin","Amit"]
print(Name[1])#Give element at that particular index.
print(Name[1:3])#Give element from 1 to 3 but does not give the 3 element.[1:] -for grabbing all element.
Name[2]="Kaash" #replace the element.
Name.extend(Number)#Merge two list.
Number.append(5)#add item at end of the list
Number.insert(2,5)#add element at the given index(index,element).
Number.remove(4)#remove an element.Number.clear()-clear whole list
Number.pop()#remove the last element.
print(Number.index(5))#tell the element is present or not. 
Number.count(4)#tell how many value are there.
Number.sort()#sort the list into asscending order.
Number.reverse()#reverse the order of the list.
print(Number)
Number2= Number.copy()#copy list
print(Number2)
#Tuples
coordinates =("101.2.109","108,0,107","100.1.100")#it is immutable.
#for tuple we use () and for list we use [].
def function(name):        #This is a function.
    print("Hello",name)

function("Piyush")

def cube(n):
    return n*n*n #return  a value

print(cube(3))

#IF/ELSE
is_male=True
is_tall=True

if is_male:
    print("You are a male and tall.")
else:
    print("You are not male and tall.")    

#Lesson 3
#Dictionaries - allow us to store information in key:value pair.
#Created inside{}.Key are unique

monthconversion={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March"
}
print(monthconversion.get("Jan"))

#Loops
i = 1
while i <= 10:
    print(i)
    i+=1
print("DONE")    

#Exponent Function
def exponent(n,N):#Function command
    num=1 
    for i in range(N): # This tell to stop (eg- N=3,will stop after 3 loops.)
        num=num*n  #num = 1,1x2=2,2x2=4,4x2=8
    return num #This will return the num with its new value.

exponent(2,3)
#2D List and nested loops
Number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(Number_grid[1][1]) #print number from the index of the 2D list.

for row in Number_grid:
    print(row)  #example for nested loops


#Lesson 4 
#Catching errors - try/Except 
try:
    number= int(input("Enter A number: "))
    print(number)      #This code check if the user has enter an int or a string.
except ValueError as e:
    print(e) # if user enter a string than this will show us the error.
#Reading Files
#"r"- stand for read."r+"-stand for read and write.
#"w"- stand for write.
#"a"- stand for append(add info at end of file).
#.readable()tell us whether or not we can run the file.
#.read()=read the file..readlines()=put all text in code  inside array .
Name_file=open("Name.txt","r+")
print(Name_file.readable())
print(Name_file.read())
Name_file.write("\nStarfire")#\n is used for new line.
Name_file.close()#Used for closing a file.

#Modules & Pip
#Module a file containing python definations and statement.
import random #used for importing different modules.
#pip - Help in installing third-party / external python module.It is a terminal command.
# use pip --version to check it version inside the terminal.

#Classes and object
#Class - It is a type of datatype that we store inside our code.
class Student:
                        #Parameter
    def __init__(self,student_id,name,marks): #__init__ -initialize function(mapping out what attribute the class should have).
        self.student_id=student_id  #This means the student id will be equal to the id given inside the report.
        self.name=name  #This means the student name  will be equal to the name given inside the report.
        self.marks=marks #This means the student marks will be equal to the marks given inside the report.

    def on_honor_roll(self): #Object Function
        if self.marks >= 80:
          return True 
        else: 
            return False

Report=Student("4535","Alex",90) #When these value are passed they are being initialized inside the Student class.
print(Report.student_id,Report.name,Report.marks)
print(Report.on_honor_roll())   

#Lesson 5
#Inheritance - combining bunch of function and attribute and inherit them in another class.It is a type of another class.
class Chef:
    def make_chicken(self):
        print("The chef can make chicken.")

    def make_salad(self):
        print("The chef can make salad.")

    def make_special_dish(self):
        print("The chef can make special dish.")

class masterchef(Chef): #Inherited the chef class into the master chef class.
    def make_bbq(self):
        print("The master chef can make bbq.")

#Lesson 6
#Polymorphism - ability to take various forms.
#Encapsulation-bundling data and methods together inside a class and controlling access to that data.
#For eg- hiding impletation of the car class inside car_calling class.
#Abstraction- hiding the internal complexity. eg- hiding self_drive inside Car class.
class Car:
    def __init__(self,brand):
        self.brand=brand

    def self_drive(self):
        print(f"My car is{self.brand} and it has self drive. ")    

class Car_calling(Car):
    def __init__(self,brand,model):  
        super().__init__(brand)
        self.model=model
    def model(self):
        print(f"The model of my {self.brand} is {self.model}")    

    def self_drive(self): #This self_drive function will override the earlier self_drive function.
        print(f"My car is {self.brand} and it not does not have self drive. ")

#This is an instance -actual object made from the blueprint(Class).
r = Car_calling("Tesla","Y")
print(r.model)
print(r.self_drive())
#In this overriding the old value is an example of polymorphism.

#Lesson 7
#Magic/Dunder method
#__len__ method- length method

class Name:
    name="Piyush"
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
res=Name()
print(res.name)     
print(len(res)) # used to find length of object inside class.

#__str__ method -string method
class NewMethod:
    Occupation ="Student"
    def __str__(self):
        return f"I am a {self.Occupation}."  #print does not work with __str__.

result =NewMethod()
print(result)  

#__repr__ method - represent method
class representmethod:
    def __repr__(self):
        Car="Bmw"
        return f"This is my {Car}." #mainly use to represent what the object is about.

c = representmethod()
print(c)    # this represented car as an object here.

#__call__ method

class dog:
    def __call__(self):
        print("woof!")
d =dog()
d()

#Lesson 8
#Dataclasses- a decorator  designed for holding data without writting boiler plate code for regular classes.
#They automatically generate __init__,__repr__ etc.

from dataclasses import dataclass

@dataclass (frozen= True)# - This will make the whole class immutable.
class Cartoon:
    name:str
    age:int
    is_alive:bool


Character = Cartoon("Naruto","28","True") #uses __repr__ to represent these as object.
Character2 =Cartoon("Sasuke","30","True")
#Character.age=-1 # Test frozen (shows error)
print(Character)
print(Character)
print(Character == Character2) # uses __eq__(equal) to check if both have same attribute or not.

# Compostion -contains/uses another class

class car:
    def start(self):
        print("Engine started.")

class vehicle:
    def __init__(self):
        self.car=car() 

    def start_car(self):
        self.car.start()

c = vehicle()
c.start_car()           

#Lesson 9
#Iterator -  an object that return one  at a time from a sequence(or data stream) and remember it position between call.
#__iter__()-return the iterator object itself.
#__next__()-return the next item in the sequence.(raises stop iterator when no more items.)
#It is object specific.Iterator concept is used inside for loop.

import random 

class dice:
    def __init__(self,rolls):
        self.rolls=rolls
        self.count=0

    def __iter__(self): #Tell the class object is iterable
        return self 

    def __next__(self): #Calls the next value from the object
            if self.count < self.rolls:
                self.count+=1
                return random.randint(1,6) #take random number between 1 and 6.
            else:
                raise StopIteration

die = dice(3)
for x in die:
    print(x)          
    
         