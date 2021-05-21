"""
CONNECT 4
"""

import numpy as np

NUMBER_COLS = 7
NUMBER_ROWS = 6
PLAYER_1 = 1
PLAYER_2 = 2


def create_board():
    """
    Create our board.
    """
    board = np.zeros((NUMBER_ROWS, NUMBER_COLS))
    return board


def drop_piece(board, row, col, piece):
    """
    Place a piece in the [row, col] spot on the
    board.
    """
    board[row][col] = piece
    return board


def is_valid_location(board, col):
    """
    Check whether chosen location is a valid one.
    """
    return board[NUMBER_ROWS - 1][col] == 0


def get_next_open_row(board, col):
    """
    Retrive empty stop
    """
    rows = board[:, col]
    return np.where(rows == 0)[0][0]


def print_board(board):
    """
    Print board
    """
    print(np.flip(board, 0))


def has_winner(board, piece):
    """
    Check whether `piece` is a winner
    """
    for col in range(NUMBER_COLS - 3):
        for row in range(NUMBER_ROWS):
            if (board[row][col] ==
                board[row][col + 1] ==
                board[row][col + 2] ==
                board[row][col + 3] == piece):
                return True

    for col in range(NUMBER_COLS):
        for row in range(NUMBER_ROWS - 3):
            if (board[row][col] ==
                board[row + 1][col] ==
                board[row + 2][col] ==
                board[row + 3][col] == piece):
                return True

    for col in range(NUMBER_COLS - 3):
        for row in range(NUMBER_ROWS - 3):
            if (board[row][col] ==
                board[row + 1][col + 1] ==
                board[row + 2][col + 2] ==
                board[row + 3][col + 3] == piece):
                return True

    for col in range(NUMBER_COLS - 3):
        for row in range(3, NUMBER_ROWS):
            if (board[row][col] ==
                board[row - 1][col + 1] ==
                board[row - 2][col + 2] ==
                board[row - 3][col + 3] == piece):
                return True
    return False


def game(board):
    """
    Game Connect4 implementation
    """
    game_over = False
    print_board(board)
    turn = PLAYER_1
    while not game_over:
        try:
            print()
            col  = int(input(f"Jogador {turn} escolha um lugar [0-6]: "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, turn)
                print_board(board)
            else:
                print("Essa coluna não possui espaços disponíveis.")
                print()
                continue

            if has_winner(board, turn):
                print(f"**** JOGADOR {turn} GANHOU ****")
                game_over = True

            if turn == PLAYER_1:
                turn = PLAYER_2
            else:
                turn = PLAYER_1
        except ValueError:
            print("Escreva um número entre 0 e 6")
            print()


if __name__ == "__main__":
    game(create_board())
