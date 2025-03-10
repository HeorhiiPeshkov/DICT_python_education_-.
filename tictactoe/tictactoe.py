def display_board(board):
    print('----------')
    for i in range(0, 9, 3):
        print(f'| {board[i]} {board[i + 1]} {board[i + 2]}|')
    print('----------')


def get_move(board):
    while True:
        try:
            x, y = map(int, input("Enter cells:").split())
            if 1 <= x <= 3 and 1 <= y <= 3:
                index = (x - 1) * 3 + (y - 1)
                if board[index] == '_':
                    return index
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Enter cells:")
        except ValueError:
            print("You should enter numbers!")


def update_board(board, move, player):
    return board[:move] + player + board[move + 1:]


def check_winner(board):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != '_':
            return board[pattern[0]]
    if '_' not in board:
        return 'Draw'
    return None


def main():
    board = '_' * 9
    current_player = 'X'
    display_board(board)
    while True:
        move = get_move(board)
        board = update_board(board, move, current_player)
        display_board(board)
        result = check_winner(board)
        if result:
            if result == 'Draw':
                print('Dead heat!')
            else:
                print(f"{result} wins!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()