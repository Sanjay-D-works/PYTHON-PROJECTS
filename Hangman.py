import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly choose something from the json file.
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return words
    
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    lives = 6
    
    #Getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join(['a','b','c' --> 'a b cd'])
        print('you have', lives , 'lives left and You have used these letters: ',' '.join(used_letters))
        
        #What current word is (ie: W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives - 1 # Takes away a life if wrong
                print("Letter is not in word.")
            
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        
        else:
            print("Invalid character. Please try again.")
    
    #Gets here when len(word_letters) == 0 OR when lives == 0.
    if lives == 0:
        print("You died ,Sorry. The Word was", word)
    else:
        print('You guessed the word', word,'!!')
    
    
hangman()
