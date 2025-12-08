from tools import clear_screen
import board
import random

def exit_game_cli()->None:
    print("Bye Bye!")
    exit(0)

def menu()->str:
    menu_input = ""

    while menu_input not in ["1", "2", "3"]:
        clear_screen()

        print("--- Morpion ---\n")
        print("1 - Jouer en solo contre l'ordinateur")
        print("2 - Jouer à deux joueurs")
        print("3 - Quitter le jeu\n")

        menu_input = str(input("Option: "))
        if menu_input in "q":
            exit_game_cli()
    
    return menu_input

def game_cpu()->None:
    winner = 0 # 1 for player 1 and 2 for cpu
    # clear_screen()
    while not winner:
        clear_screen()
        board.print_board()
        print("\n")
        if board.player_count % 2 == 0:
            user_input = input(board.player_turn_str())
            if user_input == "q":
                exit_game_cli()
            if board.fill_board(user_input):
                input("Mauvais numéro entré ou case déjà mise. Appuyez sur entrer pour continuer...")
                continue
        else:
            board.fill_board(random.randint(1, 9))

        winner = board.check_win()

        if winner == 1:
            clear_screen()
            board.print_board()
            print(f"Le joueur {winner} à gagné!")
            input("Appuyez sur entree pour sortir du jeu...")
            exit(0)
        elif winner == 2:
            clear_screen()
            board.print_board()
            print(f"L'ordinateur a gagné!")
            input("Appuyez sur entree pour sortir du jeu...")
            exit(0)
        
        if board.check_draw():
            clear_screen()
            print("Egualité...")
            input("Appuyez sur entree pour sortir du jeu...")
            exit(0)

def game_local_multiplayer()->None:
    winner = 0 # 1 for player 1 and 2 for player 2
    # clear_screen()
    while not winner:
        clear_screen()
        board.print_board()
        print("\n")
        user_input = input(board.player_turn_str())
        if user_input == "q":
            exit_game_cli()
        if board.fill_board(user_input):
            input("Mauvais numéro entré ou case déjà mise. Appuyez sur entrer pour continuer...")
            continue
        winner = board.check_win()

        if winner:
            clear_screen()
            board.print_board()
            print(f"Le joueur {winner} à gagné!")
            input("Appuyez sur entree pour sortir du jeu...")
            exit(0)
        if board.check_draw():
            clear_screen()
            board.print_board()
            print("Egualité...")
            input("Appuyez sur entree pour sortir du jeu...")
            exit(0)

def cli()->None:
    menu_input = menu()
    if menu_input == "1":
        game_cpu()
    elif menu_input == "2":
        game_local_multiplayer()
