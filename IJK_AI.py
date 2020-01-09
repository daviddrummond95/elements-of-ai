Based on skeleton code by Abhilash Kuhikar, October 2019
"""
maxdepth = 0
from logic_IJK import Game_IJK
import random
import copy
import time
# Suggests next move to be played by the current player given the current game
#
# inputs:
#     game : Current state of the game 
#
# This function should analyze the current state of the game and determine the 
# best move for the current player. It should then call "yield" on that move.


# This is the max node
def maximizechance(self, board, depth=0):
    moves = ['U', 'D', 'L', 'R']; moves_boards = []
    moves_boards =[]
    global maxdepth
# This iterates the tree across all possible moves.
    for m in moves:
        m_board = board
        self.__init__(m_board, '+', False)
        self.makeMove(m)
        m_board = self.getGame()
        moves_boards.append((m,m_board))
        # This next part determines if the depth has maxed out
        # If it has not reached maximum depth, it recursively calls the chance function which will then call the minimum function
    if depth!= (maxdepth):
        all_moves = []
        for m, m_board in moves_boards:
            utility = chance(self, m_board, '-', depth+1)
            all_moves.append((m, utility))
        max_direction, max_utility= max(all_moves, key=lambda item:item[1])

#basicall determines the best possible state at max depth. 
    if depth == maxdepth:

        max_direction, max_board = max(moves_boards,key=lambda item:eval_board(item[1]))
        max_utility = eval_board(max_board)

    return max_direction, max_utility

# This is the min node. It operates the exact same as the max node
def minimizechance(self, board, depth=0):
    moves = ['U', 'D', 'L', 'R']; moves_boards = []
    moves_boards =[]

    global maxdepth
    for m in moves:
        m_board = board
        self.__init__(m_board, '+', False)
        self.makeMove(m)
        m_board = self.getGame()
        moves_boards.append((m, m_board))
    if depth!= (maxdepth):
        all_moves = []
        for m, m_board in moves_boards:
            utility = chance(self, m_board, '+', depth)
            all_moves.append((m, utility))
        min_direction, min_utility= min(all_moves, key=lambda item:item[1])
    if depth == (maxdepth):
        min_direction, min_board = min(moves_boards,key=lambda item:eval_board(item[1]))
        min_utility= eval_board(min_board)
    return min_direction, min_utility
# chance node. Takes average utility of all possible a placements. This is really the part that will be different for the deterministic. 
def chance(self, board, currentplayer, depth= 0):
    #deterministic = self.getDeterministic()
    allboards = []
    count = 0
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            chance_board = copy.deepcopy(board)

            if chance_board[i][j] == ' ':

                if currentplayer == '+':
                    chance_board[i][j] = 'A'
                    allboards.append(chance_board)


                else:
                    chance_board[i][j] = 'a'
                    allboards.append(chance_board)
                    chance_board = copy.deepcopy(board)


    allutil = 0
    lenutil = 0
    for chance_board in allboards:

        if currentplayer == '+':
            count += 1
            direction, utility =maximizechance(self, chance_board, depth)
            allutil += utility
            lenutil += 1
        if currentplayer == '-':
            count += 1
            direction, utility =minimizechance(self, chance_board, depth)
            allutil += utility
            lenutil += 1
    if lenutil > 0:
        return (allutil/lenutil)
    else:
        return eval_board(board)
# This part is what evaluates the state of the board. It works by assigning powers of 2 to the capital and lower case letters.
# The upper case are positive and the lower case are negative
def eval_board (board):
   # values = {"A": 1, "B": 2, "C": 3, "D":4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "a": -1, "b":-2,
   #          "c": -3, "d": -4, "e": -5, "f": -6, "g": -7, "h": -8, "i": -9, "j": -10, "k": -11," ":0}
    values = {"A": 2, "B": 4, "C": 8, "D":16, "E": 32, "F": 64, "G": 128, "H": 256, "I": 512, "J": 1024, "K": float('inf'), "a": -2, "b":-4,
             "c": -8, "d": -16, "e": -32, "f": -64, "g": -128, "h": -256, "i": -512, "j": -1024, "k": -float('inf')," ":0}
    utility = 0 
    for i in range(0,len(board)-1):
        for j in range(0,len(board[i])-1):
            utility += values[board[i][j]]
    return utility
def countboard (board):
    empty = 0
    for i in range(0,len(board)-1):
        for j in range(0,len(board[i])-1):
            if board[i][j] == " ":
                empty+=1
    return empty
#deterministic is basically the minmax algorithm
def Max(self, board, depth=0):
    moves = ['U', 'D', 'L', 'R'];
    global maxdepth
    moves_boards = []

    # This iterates the tree across all possible moves.
    for m in moves:
        m_board = board
        self.__init__(m_board, '+', False)
        self.makeMove(m)
        m_board = self.getGame()
        moves_boards.append((m, m_board))
        # This part determines whether the game has ended in the search
        # If it has then it returns the utility
    if depth >= maxdepth:
        max_direction, max_board = max(moves_boards, key=lambda item: eval_board(item[1]))
        max_utility = eval_board(max_board)


    elif depth < maxdepth:
        all_moves = []
        for m, m_board in moves_boards:
            depth += 1
            utility = placepiece(self, m_board, '-', depth+1)
            all_moves.append((m, utility))
        max_direction, max_utility = max(all_moves, key=lambda item: item[1])

    # basicall determines the best possible state at max depth.


    return max_direction, max_utility
def Min(self, board, depth=0):
    moves = ['U', 'D', 'L', 'R'];
    global maxdepth
    moves_boards = []

    # This iterates the tree across all possible moves.
    for m in moves:
        m_board = board
        self.__init__(m_board, '+', False)
        self.makeMove(m)
        m_board = self.getGame()
        moves_boards.append((m, m_board))
        # This next part determines if the depth has maxed out
        # If it has not reached maximum depth, it recursively calls the chance function which will then call the minimum function
    if depth >= maxdepth:
        max_direction, max_board = min(moves_boards, key=lambda item: eval_board(item[1]))
        max_utility = eval_board(max_board)

    elif depth < maxdepth:
        all_moves = []
        for m, m_board in moves_boards:
            utility = placepiece(self, m_board, '+', depth)
            all_moves.append((m, utility))
        max_direction, max_utility = min(all_moves, key=lambda item: item[1])

    # basicall determines the best possible state at max depth.


    return max_direction, max_utility

def placepiece(self, board, currentplayer, depth=0):
    #deterministic = self.getDeterministic()
    allboards = []
    count = 0
    chance_board = copy.deepcopy(board)
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):


            if chance_board[i][j] == ' ':

                if currentplayer == '+':
                    chance_board[i][j] = 'A'



                else:
                    chance_board[i][j] = 'a'


                break



    if currentplayer == '+':

        direction, utility =Max(self, chance_board, depth)

    if currentplayer == '-':

        direction, utility =Min(self, chance_board, depth)

    return utility


def minMax(board, player, game):
    utility = 0
    #base case
#    if depth == maxdepth:
#       return utility
    #if max's turn, maxinmize the min utilities
    if player == "+":
      # for m in range(len(board)):
          utility = minimizechance(board, game)[1]
    #if min's turn, maximixze the max utilities
    if player == "-":
       for m in range(len(board)):
         utility = maximizechance(board, game)[1]
    return utility
def next_move(game: Game_IJK)-> None:

    '''board: list of list of strings -> current state of the game
       current_player: int -> player who will make the next move either ('+') or -'-')
       deterministic: bool -> either True or False, indicating whether the game is deterministic or not
    '''
    global maxdepth
    board = game.getGame()
    player = game.getCurrentPlayer()
    deterministic = game.getDeterministic()

    # You'll want to put in your fancy AI code here. For right now this just 
    # returns a random move.
    if deterministic == False:
        if countboard(board) > 8:
            maxdepth = 0
        elif countboard(board) > 5:
            maxdepth = 1
        else:
            maxdepth = 2
        if player == '+':

            start = time.time()
            best_move, _ = maximizechance(game, board)
            end = time.time()
            print(start-end)

            yield (best_move)
        if player == '-':
            best_move, _ = minimizechance(game, board)

    
            yield (best_move)


    if deterministic == True:
       if player == "+":
           maxdepth = 7
           best_move, _ = Max(game, board)

           yield(best_move)

       if player == "-":
           maxdepth = 7
           best_move, _ = Min(game, board)

           yield(best_move)
