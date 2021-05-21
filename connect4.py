"""
CONNECT 4
"""
import sys
import math
import pygame
import numpy as np


pygame.init()
pygame.font.init()


# Globals
NUMBER_COLS = 7
NUMBER_ROWS = 6
PLAYER_1 = 1
PLAYER_2 = 2
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
PIECE_COLOR = {0: BLACK, PLAYER_1: RED, PLAYER_2: YELLOW}
FONT = pygame.font.SysFont("Monospace", 40)


# Functions
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


def draw_board(board, screen):
    """
    Draw board with pygame
    """
    for col in range(board.shape[1]):
        for row in range(board.shape[0]):
            pygame.draw.rect(screen,
                             BLUE,
                             (col * SQUARESIZE, (NUMBER_ROWS - row) * SQUARESIZE,
                              SQUARESIZE,
                              SQUARESIZE))
            piece = board[row][col]
            pygame.draw.circle(screen,
                               PIECE_COLOR[piece],
                               (int((col + 1/2) * SQUARESIZE),
                                int((NUMBER_ROWS + 1/2 - row) * SQUARESIZE)),
                               RADIUS)
    pygame.display.update()


def get_screen():
    """
    Get Screen
    """
    width = NUMBER_COLS * SQUARESIZE
    height = (NUMBER_ROWS + 1) * SQUARESIZE
    size = (width, height)
    screen = pygame.display.set_mode(size)
    return screen


def game(board):
    """
    Game Connect4 implementation
    """
    width = NUMBER_COLS * SQUARESIZE
    screen = get_screen()
    game_over = False
    draw_board(board, screen)
    turn = PLAYER_1
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen,
                                   PIECE_COLOR[turn],
                                   (posx, int(SQUARESIZE / 2)),
                                   RADIUS)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, turn)

                if has_winner(board, turn):
                    label = FONT.render(f"Jogador {turn} Venceu!!", 1,
                                        PIECE_COLOR[turn])
                    screen.blit(label, (40,10))
                    game_over = True

                draw_board(board, screen)
                if turn == PLAYER_1:
                    turn = PLAYER_2
                else:
                    turn = PLAYER_1

            pygame.display.update()
    pygame.time.wait(3000)


if __name__ == "__main__":
    game(create_board())
