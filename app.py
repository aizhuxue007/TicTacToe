import os
board = {}
if os.name == 'nt':
    clear = lambda: os.system('clr')
else:
    clear = lambda: os.system('clear')


def set_up_board():
    global board, check_board
    board = {7: ' ', 8: ' ', 9: ' ',
             4: ' ', 5: ' ', 6: ' ',
             1: ' ', 2: ' ', 3: ' ', }
    check_board = [["", "", ""],
                   ["", "", ""],
                   ["", "", ""]]


def update_check_board():
    lst = list(board.values())
    for row in range(3):
        for column in range(3):
            check_board[row][column] = lst.pop(0)
    return check_board

def print_board():
    line = '---+---+---'
    clear()
    print('\n {} | {} | {}\n'.format(board[7], board[8], board[9]) +
          line + '\n {} | {} | {}\n'.format(board[4], board[5], board[6]) +
          line + '\n {} | {} | {}\n'.format(board[1], board[2], board[3]))


def update_board(x_or_o, position):
    global board
    board[position] = x_or_o.upper()


def ask_turn(x_or_o):
    if x_or_o.upper() == 'X':
        turn = input('X Move to which place? ')
        update_board('X', int(turn))
        print_board()
    elif x_or_o.upper() == 'O':
        turn = input('O Move to which place? ')
        update_board('O', int(turn))
        print_board()
    else:
        print('invalid input')


def win_indexes(n):
    # Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]


def is_winner(x_or_o):
    # size 3x3
    n = 3
    check_board = update_check_board()
    for index in win_indexes(n):
        if all(check_board[r][c] == x_or_o.upper() for r, c in index):
            return True
    return False


def cat_scan():
    if ' ' not in board.values():
        return True
    else:
        return False


def game():
    print("Welcome to Tic Tac Toes!")
    set_up_board()
    print_board()
    game_on = True
    while game_on:
        if cat_scan():
            print("Cat Scan!")
            game_on = False
        else:
            ask_turn('x')
            if not is_winner('x') and cat_scan() == False:
                ask_turn('o')
                if is_winner('o'):
                    print('O is winner!')
                    game_on = False
                elif cat_scan():
                    print("Cat Scan!")
                    game_on = False
            elif cat_scan():
                print("Cat Scan!")
                game_on = False
            else:
                print('X wins!')
                game_on = False


if __name__ == "__main__":
    game()

