from game_gui import game
import pygame
from Menu import *
from board import check_win, check_draw

def draw_finished(winner:int)->None:
    game.draw_text(f"Player {winner} wins!", game.render, game.fonts["Slackey"], game.LOGICAL_WIDTH // 2, game.LOGICAL_HEIGHT // 2, (255, 255, 255), True)

def draw_draw()->None:
    game.draw_text(f"It's a draw what a shame!", game.render, game.fonts["Slackey"], game.LOGICAL_WIDTH // 2, game.LOGICAL_HEIGHT // 2, (255, 255, 255), True)


def draw_board()->None:
    # vertical lines
    pygame.draw.line(
        game.render, (255, 255, 255), ((game.LOGICAL_WIDTH // 3), 0),
        (game.LOGICAL_WIDTH // 3, game.LOGICAL_HEIGHT), 4
    )

    pygame.draw.line(
        game.render, (255, 255, 255), ((game.LOGICAL_WIDTH // 3) * 2, 0),
        ((game.LOGICAL_WIDTH // 3) * 2, game.LOGICAL_HEIGHT), 4
    )

    # horizontal lines
    pygame.draw.line(
        game.render, (255, 255, 255), (0, (game.LOGICAL_HEIGHT // 3)),
        (game.LOGICAL_WIDTH, game.LOGICAL_HEIGHT // 3), 4
    )

    pygame.draw.line(
        game.render, (255, 255, 255), (0, (game.LOGICAL_HEIGHT // 3) * 2),
        (game.LOGICAL_WIDTH, (game.LOGICAL_HEIGHT // 3) * 2), 4
    )

def draw_moves(board)->None:
    # print(board)
    for y in range(3):
        for x in range(3):
            if board[y][x] == "X":
                game.draw_image("X", (game.LOGICAL_WIDTH // 3) * x + 150, (game.LOGICAL_HEIGHT // 3) * y)
            elif board[y][x] == "O":
                game.draw_image("O", (game.LOGICAL_WIDTH // 3) * x + 150, (game.LOGICAL_HEIGHT // 3) * y)

def multiplayer_game_render(board)->None:
    draw_board()
    draw_moves(board)
    winner = check_win()
    draw = check_draw()

    if winner:
        game.state = "win"
        print(f"Le joueur {winner} à gagné!")
        draw_finished(winner)

    if draw:
        game.state = "draw"
        print("Egualite...")
        draw_draw()

def singleplayer_game_render(board)->None:
    draw_board()

    draw_moves(board)
    winner = check_win()
    draw = check_draw()

    if winner == 1:
        game.state = "win"
        print(f"Le joueur {winner} à gagné!")
        draw_finished(winner)
    elif winner == 2:
        game.state = "win"
        print(f"L'ordinateur a gagné!")
        draw_finished(winner)
    if draw:
        game.state = "draw"
        print("Egualite...")
        draw_draw()
    