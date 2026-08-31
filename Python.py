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

# Guess Game
secret_word="Baka"
guess=""
Chances = ""

for Chances in range(1,4):
    guess = input("Enter A Word:")
    if guess == secret_word:
        print("You Won!")
        break
    elif Chances == 3:
        print("Chances Over.Better Luck Next Time.")        
    elif guess != secret_word:
        print("Try Again.")
    else:
        break
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


#Translator 
#Q- Create a translator that will convert the vowels present inside a word into "g".
def translator():
    vowels=["a","e","i","o","u","A","E","I","O","U"]

    word=str(input("Enter a word: "))
    for character in word: #This line check for the character in the word.
        if character in  vowels: #This line check for vowel present in the word.
            updated_word=word.replace(character,"g") # This word replace the vowel with "g".
            print(updated_word)
            break #break the code after it succesfull completion
    else:
        print ("Word does not contain any vowels.") 
translator()

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

Report=Student("4535","Alex","90") #When these value are passed they are being initialized inside the Student class.
print(Report.student_id,Report.name,Report.marks)   



