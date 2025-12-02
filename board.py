board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."],
]

player_count = 0

### CLI ONLY ###
def print_board()->None:
    print("-------------")
    line = ""
    for x in range(0, 3):
        line = line + "| "
        for y in range(0, 3):
            line = line + board[x][y]
            line = line + " | " 
        print(line)
        print("-------------")
        line = ""
    
def player_turn_str()->str:
    if player_count % 2 == 0:
        return "Joueur 1 (X) 1-9: "
    return "Joueur 2 (O) 1-9: "


def fill_board(pos:str)->int:
    global player_count

    pos = int(pos)
    try:
        pos = int(pos)
        if pos < 1 or pos > 9:
            return 1
        if board[(pos - 1) // 3][(pos - 1) % 3] != ".":
            return 1

        if player_count % 2 == 0:
            board[(pos - 1) // 3][(pos - 1) % 3] = "X"
        else:
            board[(pos - 1) // 3][(pos - 1) % 3] = "O"
        player_count += 1
        return 0
    except Exception as e:
        return 1