
# Board Constants
X = "X"
O = "O"
_ = " "

# This will store the board state
board = [
    [_, _, _],
    [_, _, _],
    [_, _, _]
]

def check_player_won():
    """
    Returns the player number (1 or 2) if a player has won
    If no player has won it returns None
    """

    # Checking horizontal
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == X:
            return 1
        elif board[r][0] == board[r][1] == board[r][2] == O:
            return 2

    # Checking Vertical
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == X:
            return 1
        elif board[0][c] == board[1][c] == board[2][c] == O:
            return 2

    # Diagonal 1
    if board[0][0] == board[1][1] == board[2][2] == X:
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return 2

    # Diagonal 2
    if board[0][2] == board[1][1] == board[2][0] == X:
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return 2

    return None

def print_board():
    print()
    print(" ┌───┬───┬───┐")
    for r in range(3):
        print(" │ ", end="")
        for c in range(3):
            print(board[r][c] + " │ ", end="")
        print()
        if r<2:
            print(" ├───┼───┼───┤")
    print(" └───┴───┴───┘")

def play_turn(player_num):
    global board
    if player_num%2 == 1:
        print("Player 1's turn")
    else:
        print("Player 2's turn")

    r = int(input("Enter row: "))
    c = int(input("Enter col: "))
    while board[r][c] != _:
        print("Cell {},{} is not empty".format(r,c))
        r = int(input("Enter row: "))
        c = int(input("Enter col: "))


    if player_num%2 == 1:
        board[r][c] = X
    else:
        board[r][c] = O

def main():
    player_won = None
    turn = 1

    # Play game until a player has won or the board has been filled
    while player_won is None and turn <= 9:
        print_board()
        play_turn(turn)
        player_won = check_player_won()
        turn += 1

    # Check win or draw
    if player_won == 1:
        print("PLAYER 1 WON THE GAME!")
    elif player_won == 2:
        print("PLAYER 2 WON THE GAME!")
    else:
        print("DRAW!")


main()
