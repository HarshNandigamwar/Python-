def draw_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board, marker):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == marker for i in condition):
            return True
    return False

def is_board_full(board):
    return all(space in ['X', 'O'] for space in board)

def tic_tac_toe():
    board = ['1','2','3','4','5','6','7','8','9']
    current_marker = 'X'

    while True:
        draw_board(board)
        try:
            choice = int(input(f"Player {current_marker}, choose a slot (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Invalid choice. Pick number 1-9.")
                continue
            if board[choice] in ['X', 'O']:
                print("Slot already taken, pick another.")
                continue
        except ValueError:
            print("Invalid input; please enter a number 1-9.")
            continue

        board[choice] = current_marker

        if check_winner(board, current_marker):
            draw_board(board)
            print(f"Player {current_marker} wins! Congratulations!")
            break
        if is_board_full(board):
            draw_board(board)
            print("It's a draw!")
            break

        current_marker = 'O' if current_marker == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
