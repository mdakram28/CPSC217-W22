
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

    # Write the code to check which player has won here

    # Return None if no player has won
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


def play_turn(player):
    global board
    print("Player {} turn".format(player))

    r = int(input("Enter row: "))
    c = int(input("Enter col: "))
    while board[r][c] != _:
        print("Cell {},{} is not empty".format(r,c))
        r = int(input("Enter row: "))
        c = int(input("Enter col: "))

    board[r][c] = player

def main():
    player_won = None
    turn = 1

    # Play game until a player has won or the board has been filled
    while player_won is None and turn <= 9:
        print_board()
        play_turn(X if turn%2 == 1 else O)
        player_won = check_player_won()
        turn += 1

    # Check win or draw
    if player_won is not None:
        print("PLAYER {} WON THE GAME!".format(player_won))
    else:
        print("DRAW!")


main()
