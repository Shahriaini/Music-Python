#!/usr/bin/env python

def main():
    """Start a song guessing game. """
    print("Guess the singer and his/her song!")
    
song1 = ["My Heart Will Go On"]
singer1 = ["Celine Dion"]
score = 0;
guesses = 3

def guess1song1():
        print("guess the song, in 3 guesses ")
        time.sleep(1)
        print("guesss 1, the first word out of five on this song title is My.")
        print("clue : This song became an OST for a movie that won 11 awards out of 14 nominations.")
        guess1 = input ("please enter guess, (Capital Letters For Names)")
        if guess1 !="My Heart Will Go On" :
                print(f"INCORRECT, guesses {guesses-1} guesses left.")
        if guess1 =="My Heart Will Go On":
                print("CONGRATULATION! What a genius!")
       
def guess2song1():
        print("guess 2, the second word out of five on this song title is Heart.")
        print("clue :This song became an OST for a movie that starred by Leonardo DiCaprio.")
        guess2 = input ("please enter guess,(Capital Letters For Names)")
        if guess2 !="My Heart Will Go On":
                print("INCORRECT, 1 more guesses left.")
     
        if guess2 =="My Heart Will Go On":
                print("CONGRATULATION! Let's move to the next question.")

def guess3song1():                
        print("guess 3, the third word on the this song title is Will.")
        guess3 = input ("please enter guess,(Capital Letters For Names)")
        if guess3 !="My Heart Will Go On":
                print("INCORRECT,the answer is: My Heart Will Go On.") 
        
        if guess3 =="My Heart Will Go On":
                print("CONGRATULATION!")                

def guess1singer1():
        print("Now, guess the singer of the song in 3 guesses.")
        time.sleep(1)
        print("guess1, first letter of the name is",singer1[0][0])
        guess1 = input ("please enter guess,(Capital Letters For Names)")
        if guess1 !="Celine Dion":
                print("INCORRECT,2 more guesses left")
                print("clue: She was born on 30 March 1968")
       
        if guess1 =="Celine Dion":
                print("CONGRATULATION! What a genius!")
                
            
def guess2singer1():
        print("guess2, second letter of the name is",singer1[0][1])
        guess2 = input ("please enter guess,(Capital Letters For Names)")
        if guess2 !="Celine Dion":
                print("INCORRECT,1 more guesses left")
                print("clue: She is referred as 'Queen of Power Ballads'")
        
        if guess2 =="Celine Dion":
                print("cCONGRATULATION! You did it!")
                
def guess3singer1():                
        print("guess3, third letter of the name is",singer1[0][2])
        guess3 = input ("please enter guess,(Capital Letters For Names)")
        if guess3 !="Celine Dion":
                print("INCORRECT, The answer is: Celine Dion.") 
        
        if guess3 =="Celine Dion":
                print("CONGRATULATION!")
                
import time
 
guess1song1()
guess2song1()
guess3song1()
guess1singer1()
guess2singer1()
guess3singer1()
main()