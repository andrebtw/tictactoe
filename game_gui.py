from PygameApp import *
game = PygameApp(1280, 720, False)
from Menu import *
from game_loop import *
import board
import random
import time

def quit_game()->None:
    print("Goodbye!!")
    game.pygame_close()
    exit(0)

def mouse_click_pos(event)->int:
    x, y = event.pos
    win_w, win_h = game.screen.get_size()
    x = x // (win_w / game.LOGICAL_WIDTH)
    y = y // (win_h / game.LOGICAL_HEIGHT)

    cell_w = game.LOGICAL_WIDTH  / 3
    cell_h = game.LOGICAL_HEIGHT / 3

    col = int(x // cell_w)
    row = int(y // cell_h)

    if not (0 <= row < 3 and 0 <= col < 3):
        return None

    return row * 3 + col + 1

def gui()->None:
    main_menu = Menu("Main menu", ["Play", "Settings", "Quit"], False)
    player_menu = Menu("Player menu", ["Singleplayer", "Multiplayer"], False)
    settings_menu = Menu("Settings menu", [
        "360p (640x360)",
        "720p (1280x720)",
        "1080p (1920x1080)",
        "1440p (2560x1440)",
        "4K (3840x2160)",
    ], True)
    
    game.add_font("Slackey", "Slackey-Regular.ttf", 100)
    main_menu.create_menu(game.render, game.fonts["Slackey"], game.LOGICAL_WIDTH, game.LOGICAL_HEIGHT)
    settings_menu.create_menu(game.render, game.fonts["Slackey"], game.LOGICAL_WIDTH, game.LOGICAL_HEIGHT)
    player_menu.create_menu(game.render, game.fonts["Slackey"], game.LOGICAL_WIDTH, game.LOGICAL_HEIGHT)

    game.load_image("X", "./pics/x.png", 350, 350)
    game.load_image("O", "./pics/o.png", 350, 350)

    game.state = "main_menu"

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            if game.state == "settings_menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = settings_menu.check_menu_click(event)
                    if click == "360p (640x360)":
                        game.change_res(640, 360)
                    elif click == "720p (1280x720)":
                        game.change_res(1280, 720)
                    elif click == "1080p (1920x1080)":
                        game.change_res(1920, 1080)
                    elif click == "1440p (2560x1440)":
                        game.change_res(2560, 1440)
                    elif click == "4K (3840x2160)":
                        game.change_res(3840, 2160)

            if game.state == "main_menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = main_menu.check_menu_click(event)
                    if click == "Play":
                        game.state = "player_menu"
                    elif click == "Settings":
                        game.state = "settings_menu"
                    elif click == "Quit":
                        quit_game()

            elif game.state == "player_menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = player_menu.check_menu_click(event)
                    if click == "Singleplayer":
                        game.state = "singleplayer"
                    elif click == "Multiplayer":
                        game.state = "multiplayer"

            elif game.state == "singleplayer":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    place = mouse_click_pos(event)
                    board.fill_board(place)
                    while True:
                        pos = random.randint(1, 9)
                        if board.fill_board(pos) == 0:
                            break
            
            elif game.state == "multiplayer":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    place = mouse_click_pos(event)
                    board.fill_board(place)
            
            if game.state == "win" or game.state == "draw":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.state = "main_menu"
                    board.game_restart()

        game.render.fill((0, 0, 0))
        if game.state == "main_menu":
            main_menu.draw_menu(game.render)
        elif game.state == "player_menu":
            player_menu.draw_menu(game.render)
        elif game.state == "settings_menu":
            settings_menu.draw_menu(game.render)
        elif game.state == "multiplayer":
            multiplayer_game_render(board.board)
        elif game.state == "win" or game.state == "draw":
            multiplayer_game_render(board.board)
        elif game.state == "singleplayer":
            singleplayer_game_render(board.board)

        game.pygame_draw()
