#Projects-

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

# Multiple Choice Question Quiz

import random

Questions = [
    "Q- What we use to read a file in Python?\n a.w  b. r+  c.r",
    "Q- In which year Python was implemented?\n  a.1980  b.1989  c. 1987",
    "Q- Who created Python?\n a.Guido Van Rossum   b.Brendan Eich  c.James Gosling"
]

class Logic:
    def __init__(self,q):
        self.q=q

    i = 0

    remaining =Questions.copy()
    while i < len(Questions):
        q=random.choice(remaining)
        print(q)

        if(q == "Q- What we use to read a file in Python?\n a.w  b. r+  c.r"):
            user=str(input(""))
            ans = "c"
            if (i == len(Questions)-1) and user == ans:
               print ("Correct Answer.Quiz Ended")
            elif user == ans:
               print("Correct Answer.Moving to next question.")    
        elif (q == "Q- In which year Python was implemented?\n  a.1980  b.1989  c. 1987" ):
            user2=str(input(""))
            ans2 ="b"
            if (i == len(Questions)-1) and user2 == ans2:
               print ("Correct Answer.Quiz Ended")
            elif user2 == ans2 :
               print("Correct Answer.Moving to next question")
        elif (q == "Q- Who created Python?\n a.Guido Van Rossum   b.Brendan Eich  c.James Gosling"):
            user3=str(input(""))
            ans3 = "a"            
            if (i == len(Questions)-1) and user3 == ans3:
              print ("Correct Answer.Quiz Ended")
            elif user3 == ans3:
              print("Correct Answer.Moving to next question.") 
        else:
           print("There was an error starting the Logic.")


        remaining.remove(q)
        i+=1         

        if i == len(Questions):
            break
        
Logic("q") 