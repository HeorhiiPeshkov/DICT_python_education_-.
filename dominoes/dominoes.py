import random


def create_dominoes():
    dominoes = []
    for a in range(7):
        for b in range(a, 7):
            dominoes.append([a, b])
    return dominoes


def dominoes_shuffle(dominoes):
    random.shuffle(dominoes)
    player = dominoes[:7]
    computer = dominoes[7:14]
    stock = dominoes[14:]
    return player, computer, stock


def find_starting_double(player, computer):
    for value in range(6, -1, -1):
        piece = [value, value]
        if piece in player:
            player.remove(piece)
            return 'player', piece
        if piece in computer:
            computer.remove(piece)
            return 'computer', piece
    return None, None


def status(domino_snake, player, computer, stock):
    print('=' * 100)
    print(domino_snake)
    print('Your dominoes')
    for a, piece in enumerate(player):
        print(f'{a + 1}: {piece}')
    print(f'Computer dominoes: {len(computer)} | Stock: {len(stock)}')
    print('=' * 100)


def can_be_put(piece, domino_snake, side):
    if side == 'left':
        return piece[0] == domino_snake[0][0] or piece[1] == domino_snake[0][0]
    elif side == 'right':
        return piece[0] == domino_snake[-1][1] or piece[1] == domino_snake[-1][1]
    return False


def make_move(domino_snake, piece, side):
    if side == 'left':
        if piece[1] == domino_snake[0][0]:
            domino_snake.insert(0, piece)
        else:
            domino_snake.insert(0, piece[::-1])
    elif side == 'right':
        if piece[0] == domino_snake[-1][1]:
            domino_snake.append(piece)
        else:
            domino_snake.append(piece[::-1])


def player_turn(player, stock, domino_snake):
    while True:
        move = input('Your turn! Put domino you want:\n>')
        if move.isdigit():
            move = int(move)
            if move == 0:
                if stock:
                    drawn = stock.pop()
                    player.append(drawn)
                    print(f'You drew: {drawn}')
                else:
                    print('Stock is empty. Cant draw')
                break
            elif 1 <= move <= len(player):
                piece = player[move - 1]
                side = input('Choose where to place domino (choose left or right side):\n>').strip().lower()
                if side in ['left', 'right']:
                    if can_be_put(piece,domino_snake, side):
                        make_move(domino_snake, piece, side)
                        player.pop(move - 1)
                        break
                    else:
                        print('Invalid side.')
                else:
                    print('Incorrect input!')
            else:
                print('Cant be put')
        else:
            print('Incorrect input!')


def computer_turn(computer, domino_snake, stock):
    for a, piece in enumerate(computer):
        if can_be_put(piece, domino_snake, 'left'):
            make_move(domino_snake, piece, 'left')
            computer.pop(a)
            return
        elif can_be_put(piece, domino_snake, 'right'):
            make_move(domino_snake, piece, 'right')
            computer.pop(a)
            return
    if stock:
        computer.append(stock.pop())


def check_end(player, computer, stock):
    if not player:
        return 'You won!'
    elif not computer:
        return 'Computer won!'
    elif not stock:
        return 'Draw!'
    return None


def main():
    dom = create_dominoes()
    player, computer, stock = dominoes_shuffle(dom)
    turn, piece = find_starting_double(player, computer)
    if not piece:
        print('Game cant be started')
        return
    domino_snake = [piece]
    turn = 'computer' if turn == 'player' else 'player'
    while True:
        status(domino_snake, player, computer, stock)
        result = check_end(player, computer, stock)
        if result:
            print(result)
            break
        if turn == 'player':
            player_turn(player, stock, domino_snake)
            turn = 'computer'
        else:
            print('Computers turn')
            computer_turn(computer, domino_snake, stock)
            turn = 'player'


if __name__ == '__main__':
    main()
