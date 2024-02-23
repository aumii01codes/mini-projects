#MINI GAME: ROCK PAPER SCISSOR CUT
import random

def play(input):
    choice_list = ['scissor', 'rock', 'paper']
    com_input =random.choice(choice_list)
    user = 0 #score of the player
    comp = 0 #score of computer

    if input == com_input:
        user += 0
        comp += 0
    
    elif input ==  'rock' and com_input == 'paper':
        comp += 1
    
    elif input ==  'rock' and com_input == 'scissor':
        user += 1

    elif input ==  'scissor' and com_input == 'paper':
        user += 1

    elif input ==  'scissor' and com_input == 'rock':
        comp += 1

    elif input ==  'paper' and com_input == 'scissor':
        comp += 1

    elif input ==  'paper' and com_input == 'rock':
        user += 1
    
    score =[]
    score.extend(user, comp)
    return score

def quit():
    break

def help():
    print('The game resembles our childhood favourite game of rock paper scissor cut.')
    print('Give input as per needed.')
    print('Between rock and paper, paper wins')
    print('Between scissor and paper, scissor wins')
    print('Between rock and scissor, rock wins')

while True:
    print('Enter \'play\' to play the game')
    print('Enter \'help\' to know the rules')
    print('Enter \'quit\' to quit from the game')
    user_input = input()

    if user_input == 'play':
        game_input = input('Enter either of \'rock\', \'paper\' or \'scissor\' : ')
        scoreplay(game_input)
    
    elif user_input == 'help':
        help()
    
    elif user_input == 'quit':
        quit()

    else:
        print('Invalid input! Read the rules.')
