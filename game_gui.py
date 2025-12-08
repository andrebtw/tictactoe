from PygameApp import *
game = PygameApp(1280, 720, False)
from Menu import *

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
            print(game.state)
            if game.state == "main_menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print("dzdzdzddzdzdz down")
                    pass
                click = main_menu.check_menu_click(event)
                game.render.fill((0, 0, 0))
                main_menu.draw_menu(game.render)
                game.pygame_draw()
                if click == "Play":
                    game.state = "player_menu"

            if game.state == "player_menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print("dzdzdzddzdzdz down")
                    pass
                click = player_menu.check_menu_click(event)
                game.render.fill((0, 0, 0))
                player_menu.draw_menu(game.render)
                game.pygame_draw()
                if click == "Singleplayer":
                    game.state = "player_menu"