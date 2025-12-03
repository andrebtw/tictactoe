board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."],
]

winning_pos = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
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
###############

def fill_board(pos:str)->int:
    global player_count, board

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

def check_win()->int:
    global board, winning_pos

    sign = "X"
    for combo in winning_pos:
        if board[(combo[0] - 1) // 3][(combo[0] - 1) % 3] == sign and board[(combo[1] - 1) // 3][(combo[1] - 1) % 3] == sign and board[(combo[2] - 1) // 3][(combo[2] - 1) % 3] == sign:
            return 1

    sign = "O"
    for combo in winning_pos:
        if board[(combo[0] - 1) // 3][(combo[0] - 1) % 3] == sign and board[(combo[1] - 1) // 3][(combo[1] - 1) % 3] == sign and board[(combo[2] - 1) // 3][(combo[2] - 1) % 3] == sign:
            return 2
    
    return 0

def check_draw()->int:
    global board

    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] == ".":
                return 0
    return 1
