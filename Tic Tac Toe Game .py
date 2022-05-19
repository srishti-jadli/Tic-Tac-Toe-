#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def display_board(board):
    print('     |      |     ')
    print(' '+board[7]+'   |   '+board[8]+'  |  '+board[9])
    print('     |      |     ')
    print('-----|------|-----')
    print('     |      |     ')
    print(' '+board[4]+'   |   '+board[5]+'  |  '+board[6])
    print('     |      |     ')
    print('-----|------|-----')
    print('     |      |     ')
    print(' '+board[1]+'   |   '+board[2]+'  |  '+board[3])


# In[2]:


def player_input():
    choice=' '
    while choice not in ['X','O']:
        choice=input('Please select x or o: ').upper()
        if choice not in ['X','O']:
            print('Sorry invalid choice!!!')
    if choice=="X":
        return ("X","O")
    else:
        return ("O","X")


# In[3]:


def place_marker(board, marker, position):
    board[position]=marker 


# In[4]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 


# In[5]:


import random 

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# In[6]:


def space_check(board, position):
    return board[position]== ' '


# In[7]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[8]:


def player_choice(board):
    choice=' '
    in_range= range(1,10)
    validity=False 
    while not choice.isdigit() or validity==False:
        choice=input("Please enter a number between 1 to 9: ")
        if choice.isdigit()==False:
            print('Sorry invalid input!!!')
        if choice.isdigit():
            if int(choice) in in_range:
                validity=True 
            else:
                print('Sorry Out of range!!!')
                validity=False 
    return int(choice)
    


# In[9]:


def replay():
    choice=' '
    while choice not in ['Y','N']:
        choice=input("Do you wish to continue \nY for Yes or N for No: ").upper()
        if choice not in ['Y','N']:
            print("Sorry invalid choice!!!")
    if choice == "Y":
        return True 
    else:
        return False 


# In[10]:


print("TIC TAC TOE")

while True:
    the_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker,player2_marker = player_input()
    turn=choose_first()
    print(f'{turn} will go first!!')
    display_board(the_board)
    
    player_command=input('Do you wish to play: ').lower()
    
    if player_command[0]=='y':
        game_on=True 
    else:
        game_on=False 
    
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker, position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Congratulations! you won the game!!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Draw!!")
                    break
                else:
                    turn='Player 2'
        
        else: 
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker, position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Congrats you WON!!!")
                game_on=False 
            else:
                if full_board_check(the_board):
                    print("It's a Draw!!")
                    break
                else:
                    turn='Player 1'

    if not replay():
        break 
            


# In[ ]:




