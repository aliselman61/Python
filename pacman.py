import os
import sys
import termios
import tty

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class Game:
    def __init__(self):
        self.maze = [
            "###################",
            "#........#........#",
            "#.###.###.#.###.###",
            "#.#....... ....#.#",
            "#.#.###.#####.###.#",
            "#.#.#.#...#...#.#.#",
            "#.#.#.###.#.###.#.#",
            "#.#.#.#.......#.#.#",
            "#.#.#.###.#####.#.#",
            "#.................#",
            "###################"
        ]
        self.player_pos = [1, 1]
        self.exit_pos = [9, 17]
    
    def draw_maze(self):
        os.system('clear')
        for y, row in enumerate(self.maze):
            for x, char in enumerate(row):
                if [y, x] == self.player_pos:
                    print("P", end="")
                else:
                    print(char, end="")
            print()
        print("Use arrow keys to move. Press 'q' to quit.")
    
    def move_player(self, direction):
        y, x = self.player_pos
        if direction == 'up' and self.maze[y - 1][x] != '#':
            self.player_pos[0] -= 1
        elif direction == 'down' and self.maze[y + 1][x] != '#':
            self.player_pos[0] += 1
        elif direction == 'left' and self.maze[y][x - 1] != '#':
            self.player_pos[1] -= 1
        elif direction == 'right' and self.maze[y][x + 1] != '#':
            self.player_pos[1] += 1
    
    def play(self):
        self.draw_maze()
        while True:
            key = get_key()
            if key == '\x1b':  # ESC sequence
                key = get_key()
                if key == '[':
                    key = get_key()
                    if key == 'A':
                        self.move_player('up')
                    elif key == 'B':
                        self.move_player('down')
                    elif key == 'C':
                        self.move_player('right')
                    elif key == 'D':
                        self.move_player('left')
            elif key == 'q':
                break
            self.draw_maze()

if __name__ == "__main__":
    game = Game()
    game.play()