import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


BOARD = [[(y == 0 and x or x == 0 and y) or '-' for x in range(4)] for y in range(4)]
BOARD[0][0] = 'y\\x'


def input_player(player):
    print(f'Ход игрока: {player}')
    coordinates = input('Введите координаты\nпример "2 1"\nВвод:').split()
    coordinates = list(filter(lambda x: x.isdigit() and 0 < int(x) < len(BOARD), coordinates))

    if len(coordinates) == 2:
        x, y = map(int, coordinates)
    else:
        print(f"Некорректный ввод !")
        return input_player(player)

    return x, y


def insert_cord(x, y, player):
    if BOARD[x][y] == '-':
        if player == 'player1':
            BOARD[x][y] = 'X'
        else:
            BOARD[x][y] = 'O'
        return True
    return False


def print_board():
    for board_x in BOARD:
        for board_y in board_x:
            print(f'{board_y}', end='\t')
        print()


def x_line(source):
    for board_line in BOARD:
        count_line = len(list(filter(lambda x: x == source, board_line)))
        if count_line == 3:
            return True
    return False


def xy_line(source):
    xy = []
    for index, board_line in enumerate(BOARD[1:], start=1):
        xy.append(BOARD[index][index])
        count_line = len(list(filter(lambda x: x == source, xy)))
        if count_line == 3:
            return True
    return False


def yx_line(source):
    xy = []
    for index, board_line in enumerate(BOARD[1:], start=0):
        board_line = board_line[1:]
        board_line.reverse()
        if index < 3:
            xy.append(board_line[index])

        count_line = len(list(filter(lambda x: x == source, xy)))
        if count_line == 3:
            return True
    return False


def y_line(source):
    for i, line in enumerate(BOARD):
        count_line = 0
        for j, _ in enumerate(line):
            if BOARD[j][i] == source:
                count_line += 1
        if count_line == 3:
            return True
    return False


def no_body():
    for line in BOARD:
        a = any(filter(lambda x: x == '-', line))
        if a:
            return False
    return True


def win(source='X'):
    return x_line(source) or y_line(source) or xy_line(source) or yx_line(source)


def game():
    player = ['player1', 'player2', ]
    source = ['X', 'O']
    index = 0
    win_payer = False
    while not win_payer:
        cls()
        print_board()
        x, y = input_player(player[index])
        result = insert_cord(x, y, player[index])
        n_body = no_body()
        win_payer = win(source[index])
        win_payer = win_payer or n_body
        if not win_payer and result:
            index ^= 1
        else:
            continue

    cls()
    if n_body:
        print('Ничья!!!')
        return
    print_board()
    print(f'Winner {player[index]}')
    print('END GAME')


if __name__ == '__main__':
    game()
