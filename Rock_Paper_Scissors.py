# Rock Paper Scissors

import random

def play():
    user = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return 'It\'s is a Tie'
        
    if is_win(user, computer):
        return 'You Win!'
        
    return 'You Lose!'
    
def is_win(player,opponent):
        #return true if player is wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
            
            
print(play())
