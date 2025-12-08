from game_gui import game
import pygame
from board import *

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

def multiplayer_game_render()->None:
    draw_board()
    winner = check_win()

    if winner:
        print(f"Le joueur {winner} à gagné!")
    if check_draw():
        print("Egualité...")