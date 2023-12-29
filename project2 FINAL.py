"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tomas Horniak
email: tomas.horniak27@gmail.com
discord: just#7854
"""

separator = "========================================"

print("Welcome to Tic Tac Toe"
"\n========================================"
"\nGAME RULES:"
"\nEach player can place one mark (or stone)"
"\nper turn on the 3x3 grid. The WINNER is"
"\nwho succeeds in placing three of their"
"\nmarks in a:"
"\n* horizontal,"
"\n* vertical or"
"\n* diagonal row"
"\n========================================"
"\nLet's start the game"
)

#show and def play board

def show_board(board):
    print("+---+---+---+")
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("+---+---+---+")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("+---+---+---+")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print("+---+---+---+")

#choose position in board

def choose_position(player):
    while True:
        player_move = input(f"Player {player}, please enter your move number (1-9): ")
        if player_move.isdigit() and 1 <= int(player_move) <= 9:
            return int(player_move) - 1
        else:
            print ("Invalid move. Enter number between 1 and 9")

# def check if it's correct move
            
def is_correct_move(player_move, board):
    row = player_move // 3
    column = player_move % 3
    
    if board[row][column] == " ":
        return True
    else:
        print("This position is already occupied. Please choose another one.")
        return False

# def perform a move
 
def perform_move(player_move, player, board):
    column = player_move // 3
    row = player_move % 3
    board[column][row] = player

# def check if it's win

def win(player, board):
    for d in range(3):
        # check columns
        if board [0][d] == player and board [1][d] == player and board [2][d] == player:
            return True
        # check rows
        if board [d][0] == player and board [d][1] == player and board [d][2] == player:
            return True
    #check diagonals a)
       
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    #check diagonals b)

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# def check if it's tie

def tie(board):
    for column in board:
        if " " in column:
            return False
    return True


#9. Jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy


# def start game

def start_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    show_board(board)
    while True:
        player_move = choose_position(player)
        while not is_correct_move(player_move, board):
            player_move = choose_position(player)
            continue
        perform_move(player_move, player, board)
        show_board(board)
        if win(player, board):
            print(f"Congratulations, the player {player} WON")
            break
        if tie(board):
            print("It's a tie")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

start_game()       