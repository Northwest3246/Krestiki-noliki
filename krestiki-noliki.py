def print_board(board):
    """Функция для отображения текущего состояния игрового поля."""
    print("Текущее состояние игрового поля:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Функция для проверки, есть ли победитель или ничья."""
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]  # Возвращаем выигравший символ

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Проверка на ничью
    if all(cell != " " for row in board for cell in row):
        return "Ничья"

    return None  # Игра продолжается


def is_valid_move(board, row, col):
    """Проверка корректности ввода и возможности сделать ход."""
    if 0 <= row < 3 and 0 <= col < 3:
        return board[row][col] == " "
    return False


def main():
    """Главная функция игры."""
    # Инициализация пустого поля 3x3
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Получаем ввод от игрока
        try:
            row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
            col = int(input(f"Игрок {current_player}, введите номер столбца (0-2): "))
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите целое число.")
            continue

        # Проверка корректности хода
        if not is_valid_move(board, row, col):
            print("Некорректный ход! Попробуйте еще раз.")
            continue

        # Ставим символ текущего игрока на поле
        board[row][col] = current_player

        # Проверка на победителя
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Ничья":
                print("Игра завершилась ничьей!")
            else:
                print(f"Игрок {winner} победил!")
            break

        # Смена игрока
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()





