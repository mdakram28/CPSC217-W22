# hello_psg.py

import PySimpleGUI as sg

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
    Returns the player (X or O) if a player has won
    If no player has won it returns None
    """

    # Checking horizontal
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2]:
            if board[r][0] != _:
                return board[r][0]

    # Checking Vertical
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            if board[0][c] != _:
                return board[0][c]

    # Diagonal 1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != _:
            return board[0][0]

    # Diagonal 2
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != _:
            return board[0][2]

    return None

props_btn = {
    'size': (3,2)
}
layout = [
    [sg.Text('Turn: X', key="turn")],
    [sg.Button(_, key="00", **props_btn), sg.Button(_, key="01", **props_btn), sg.Button(_, key="02", **props_btn)],
    [sg.Button(_, key="10", **props_btn), sg.Button(_, key="11", **props_btn), sg.Button(_, key="12", **props_btn)],
    [sg.Button(_, key="20", **props_btn), sg.Button(_, key="21", **props_btn), sg.Button(_, key="22", **props_btn)]
]
# Create the window
window = sg.Window("Tic-Tac-Toe", layout)

def show_board(turn):
    window["turn"].Update("Turn: " + (X if turn % 2 == 1 else O))
    for r in range(3):
        for c in range(3):
            window[str(r)+str(c)].Update(board[r][c], disabled=board[r][c]!=_)

def main():
    turn = 1
    player_won = None
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break
        for r in range(3):
            for c in range(3):
                if event == (str(r) + str(c)) and player_won is None:
                    print("Pressed: ", r, c)
                    if board[r][c] == _:
                        board[r][c] = X if turn % 2 == 1 else O

                        player_won = check_player_won()
                        # Update turn and show board
                        turn += 1
                        show_board(turn)

        if player_won is not None:
            window["turn"].Update("PLAYER {} WON!".format(player_won))
        elif turn > 9:
            window["turn"].Update("DRAW!")

    window.close()

main()
