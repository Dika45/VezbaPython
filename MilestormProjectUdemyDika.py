#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


# In[2]:


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']


# In[7]:


display(row1,row2,row3)


# In[6]:


row2[1] = 'X'


# In[8]:


input("Please enter a value: ")


# In[9]:


result = input("Please enter a value: ")


# In[10]:


result


# In[11]:


result = input("Enter Value: ")


# In[12]:


result_int = int(result)


# In[13]:


type(result_int)


# In[15]:


position_index = int(input("Choose an index position: "))


# In[18]:


row1[position_index]


# In[1]:


def user_choice():
    
    choice = 'WRONG'
    
    while choice.isdigit() == False:
        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
    
    return int(choice)


# In[2]:


user_choice()


# In[23]:


some_value = '100'


# In[24]:


some_value.isdigit()


# In[3]:


def user_choice():
    
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False
    
    
    
    while choice.isdigit() == False or within_range == False:
        
        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of range (0-10)")
                within_range = False
    
    return choice


# In[4]:


user_choice()


# In[5]:


game_list = [0,1,2]


# In[9]:


def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


# In[10]:


display_game(game_list)


# In[11]:


def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice! ")
    
    return int(choice)


# In[12]:


position_choice()


# In[13]:


def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at position: ")
    
    game_list[position] = user_placement
    
    return game_list


# In[14]:


replacement_choice(game_list,1)


# In[16]:


def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        
        choice = input("Keep playing? (Y or N) ")
        
        if choice not in ['Y','N']:
            print("Sorry, I dont undestand, plase choose Y or N ")
    
    if choice == "Y":
        return True
    else:
        return False


# In[19]:


gameon_choice()


# In[20]:


game_on = True
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    dispaly_game(game_list)
    
    game_on = gameon_choice()


# In[14]:


from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[15]:


def player_input():
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()
        
    if marker == 'X':
        
        return('X','O')
    else:
        return('O','X')


# In[4]:


player1_marker, player2_marker = player_input()


# In[5]:


player2_marker


# In[16]:


def place_marker(board, marker, position):
    
    board[position] = marker


# In[17]:


def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))


# In[18]:


import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[19]:


def space_check(board, position):
    
    return board[position] == ' '


# In[20]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True


# In[21]:


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        
    return position


# In[25]:


def replay():
    
    choice = input("Play again? Enter Yes or No")
    
    return choice == 'Yes'


# In[27]:


# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to iks oks')

while True:
    
    # PLAY THE GAME
    
    ## SET EVERYTHING UP (BOARD,WHOS FIRST CHOOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input('Ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    ## GAME PLAY
    
    while game_on:
        
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
            
        
        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            # Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'
            
            
        
    if not replay():
        break
# BREAK OUT OF THE WHILE LOOP ON replay()


# 

# In[ ]:




