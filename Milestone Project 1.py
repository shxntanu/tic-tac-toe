import os
import random

board = ['#',1,2,3,4,5,6,7,8,9]
def display_board(board):

    print("\n")
    print("{:<5}  {:<5}  {:<5}".format(board[1],board[2],board[3]))
    print('---------------')

    print("{:<5}  {:<5}  {:<5}".format(board[4],board[5],board[6]))

    print('---------------')

    print("{:<5}  {:<5}  {:<5}".format(board[7],board[8],board[9]))
    print("\n")

def player_input():
    marker = ""

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    
    board[position]=marker


def win_check(board,mark): #returns True if the mark has won
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first(players):
    return random.choice(players)

def space_check(board,position): #returns True if space is available

    return board[position] in [1,2,3,4,5,6,7,8,9]

def board_full(board): #returns True if board is full
    
    return 1 not in board and 2 not in board and 3 not in board and 4 not in board and 5 not in board and 6 not in board and 7 not in board and 8 not in board and 9 not in board

def player_choice(board,char):

    position = int(input("Enter your next position ({}): ".format(char)))

    if space_check(board,position):
        return position
    else:
        print("That space is occupied")
        player_choice(board,char)

def replay():

    again = input("Do you want to play again (Y for yes and N for no): ")
    if again == 'Y':
        return True
    elif again == 'N':
        return False
    else:
        print("Wrong Input!")
        replay()

print("Welcome to Tic-Tac-Toe!")
display_board(board)

P1,P2 = player_input()

turn = choose_first([1,2])

while(True):

    if turn ==1:
            
        pos= player_choice(board,P1)

        if not board_full(board):

            if space_check(board,pos):

                place_marker(board,P1,pos)
                os.system('clear')
                display_board(board)
                turn =2
                if win_check(board,P1):
                    P1= P1 + "has won!"
                    print(P1)
                    break
            
    elif turn ==2:

        pos= player_choice(board,P2)

        if not board_full(board):

            if space_check(board,pos):

                place_marker(board,P2,pos)
                os.system('clear')
                display_board(board)
                turn =1
                if win_check(board,P2):
                    P2 = P2 + " has won!"
                    print(P2)
                    break