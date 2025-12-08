from PygameApp import *
game = PygameApp(1280, 720, False)
from Menu import *
from game_loop import *
from board import *

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
    game.add_font("Slackey", "Slackey-Regular.ttf", 100)
    main_menu.create_menu(game.render, game.fonts["Slackey"], game.LOGICAL_WIDTH, game.LOGICAL_HEIGHT)
    player_menu.create_menu(game.render, game.fonts["Slackey"], game.LOGICAL_WIDTH, game.LOGICAL_HEIGHT)
    
    game.state = "main_menu"

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

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
            
            elif game.state == "multiplayer":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    fill_board(mouse_click_pos(event))

        game.render.fill((0, 0, 0))
        if game.state == "main_menu":
            main_menu.draw_menu(game.render)
        elif game.state == "player_menu":
            player_menu.draw_menu(game.render)
        elif game.state == "multiplayer":
            multiplayer_game_render()

        game.pygame_draw()
