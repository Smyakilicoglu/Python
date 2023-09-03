# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:13:49 2023

@author: Sümeyra KILIÇOĞLU
"""

#Step 4

import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                  
print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["elma", "armut", "muz", "çilek", "karpuz", "portakal", "kavun", "üzüm", "erik", "şeftali", "kiraz", "vişne", "kivi", "ananas", "nar", "mandalina", "limon", "greyfurt", "üzüm", "şekerpare"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}" )
while not end_of_game:
    guess = input("Bir harf söyleyin: ").lower()
    if guess in display:
        print("Bu harfi daha önce tahmin etmiştiniz.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
      print(f"{guess} harfi boşluklardan birinde değil. Kaybediyorsun")
      lives -= 1
      print(f"{stages[lives]}")
      if lives == 0:
        end_of_game = True
        print("Kaybettin.")
        print(chosen_word)
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Kazandın.")