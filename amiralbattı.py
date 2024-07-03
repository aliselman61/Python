import random

# Oyun tahtası boyutu
BOARD_SIZE = 10
SHIP_LENGTHS = [5, 4, 3, 3, 2,]

def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]

def print_board(board):
    print("  " + " ".join([chr(i) for i in range(65, 65 + BOARD_SIZE)]))
    for idx, row in enumerate(board):
        print(f"{idx} " + " ".join(row))

def is_valid_placement(board, ship_length, row, col, orientation):
    if orientation == 'H':
        if col + ship_length > BOARD_SIZE:
            return False
        for i in range(ship_length):
            if board[row][col + i] != '~':
                return False
    else:
        if row + ship_length > BOARD_SIZE:
            return False
        for i in range(ship_length):
            if board[row + i][col] != '~':
                return False
    return True

def place_ship(board, ship_length):
    while True:
        orientation = random.choice(['H', 'V'])
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if is_valid_placement(board, ship_length, row, col, orientation):
            if orientation == 'H':
                for i in range(ship_length):
                    board[row][col + i] = 'S'
            else:
                for i in range(ship_length):
                    board[row + i][col] = 'S'
            break

def take_shot(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'
        return True
    elif board[row][col] == '~':
        board[row][col] = 'O'
        return False
    return None

def all_ships_sunk(board):
    for row in board:
        if 'S' in row:
            return False
    return True

def main():
    user_board = create_board(BOARD_SIZE)
    computer_board = create_board(BOARD_SIZE)
    hidden_board = create_board(BOARD_SIZE)
    
    for ship_length in SHIP_LENGTHS:
        place_ship(user_board, ship_length)
        place_ship(computer_board, ship_length)

    print("Amiral Battı Oyununa Hoş Geldiniz!")
    print_board(hidden_board)
    
    while True:
        print("\nKendi Tahtanız:")
        print_board(user_board)
        
        print("\nBilgisayarın Tahtası:")
        print_board(hidden_board)
        
        try:
            shot = input("Atış yapmak için koordinat girin (örn. A5): ").upper()
            col = ord(shot[0]) - 65
            row = int(shot[1:])
        except (IndexError, ValueError):
            print("Geçersiz koordinat. Tekrar deneyin.")
            continue

        if take_shot(computer_board, row, col):
            print("Vuruldu!")
            hidden_board[row][col] = 'X'
        else:
            print("Iska!")
            hidden_board[row][col] = 'O'
        
        if all_ships_sunk(computer_board):
            print("Tebrikler! Bilgisayarın tüm gemilerini batırdınız!")
            break
        
        comp_row = random.randint(0, BOARD_SIZE - 1)
        comp_col = random.randint(0, BOARD_SIZE - 1)
        while take_shot(user_board, comp_row, comp_col) is None:
            comp_row = random.randint(0, BOARD_SIZE - 1)
            comp_col = random.randint(0, BOARD_SIZE - 1)
        
        if take_shot(user_board, comp_row, comp_col):
            print(f"Bilgisayar {chr(comp_col + 65)}{comp_row} koordinatında vurdu!")
        else:
            print(f"Bilgisayar {chr(comp_col + 65)}{comp_row} koordinatında ıskaladı!")
        
        if all_ships_sunk(user_board):
            print("Maalesef, bilgisayar tüm gemilerinizi batırdı.")
            break
        
if __name__ == "__main__":
    main()
    