
import time


# ==========================================
# CLASS 1: PLAYER
# Stores information about each player
# ==========================================

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.moves = 0
        self.result = "In progress"
        self.time_played = 0.0

    def record_move(self):
        self.moves += 1

    def __str__(self):
        return f"{self.name} ({self.color})"


# ==========================================
# CLASS 2: CHECKER
# Represents one checker on the board
# ==========================================

class Checker:
    def __init__(self, color, king=False):
        self.color = color
        self.king = king

    def directions(self):
        # Kings can move forward and backward.
        if self.king:
            return [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Red moves toward row 0.
        if self.color == "r":
            return [(-1, -1), (-1, 1)]

        # Black moves toward row 7.
        return [(1, -1), (1, 1)]

    def promote(self, row):
        if self.color == "r" and row == 0:
            self.king = True
        elif self.color == "b" and row == 7:
            self.king = True

    def __str__(self):
        if self.king:
            return self.color.upper()
        return self.color


# ==========================================
# CLASS 3: BOARD
# Stores the board and implements move rules
# ==========================================

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup()

    def setup(self):
        # Black checkers occupy the top three rows.
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Checker("b")

        # Red checkers occupy the bottom three rows.
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Checker("r")

    def inside(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def display(self):
        print("\n    a b c d e f g h")
        print("   -----------------")

        for row in range(8):
            cells = []

            for col in range(8):
                piece = self.grid[row][col]
                cells.append(str(piece) if piece else ".")

            print(f"{8 - row} | " + " ".join(cells)
                  + f" | {8 - row}")

        print("   -----------------")
        print("    a b c d e f g h")
        print("r/R = red checker/king; b/B = black checker/king")
        print(f"Pieces left: red {self.count_pieces('r')}, "
              f"black {self.count_pieces('b')}")

    def legal_moves(self, color):
        moves = []
        captures = []

        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]

                if piece is None or piece.color != color:
                    continue

                for dr, dc in piece.directions():
                    r1, c1 = row + dr, col + dc
                    r2, c2 = row + 2 * dr, col + 2 * dc

                    # Normal diagonal move.
                    if self.inside(r1, c1):
                        target = self.grid[r1][c1]

                        if target is None:
                            moves.append(
                                ((row, col), (r1, c1), None)
                            )

                        # Capture an opponent's checker.
                        elif (
                            target.color != color
                            and self.inside(r2, c2)
                            and self.grid[r2][c2] is None
                        ):
                            captures.append(
                                ((row, col), (r2, c2), (r1, c1))
                            )

        # Captures are compulsory.
        return captures if captures else moves

    def move(self, start, end, color):
        for source, destination, captured in self.legal_moves(color):
            if source == start and destination == end:
                piece = self.grid[start[0]][start[1]]

                # Was the checker already a king?
                was_king = piece.king

                self.grid[end[0]][end[1]] = piece
                self.grid[start[0]][start[1]] = None

                if captured is not None:
                    self.grid[captured[0]][captured[1]] = None

                # Promote if the checker reaches the last row.
                piece.promote(end[0])
                promoted = not was_king and piece.king

                # Return whether a capture and promotion occurred.
                return captured is not None, promoted

        raise ValueError("Illegal move. Try again.")

    def count_pieces(self, color):
        return sum(
            1
            for row in self.grid
            for piece in row
            if piece is not None and piece.color == color
        )


# ==========================================
# CLASS 4: GAME
# Controls turns, timing and game summary
# ==========================================

class Game:
    def __init__(self, name1, name2):
        self.players = [
            Player(name1, "r"),
            Player(name2, "b")
        ]

        self.board = Board()
        self.current = 0
        self.total_moves = 0
        self.start_time = time.monotonic()
        self.end_time = None
        self.finished = False
        self.winner = None

        # Stores the position of a checker that must
        # continue a multiple-capture sequence.
        self.must_capture_from = None

    def current_player(self):
        return self.players[self.current]

    def parse_square(self, text):
        text = text.strip().lower()

        if (
            len(text) != 2
            or text[0] not in "abcdefgh"
            or text[1] not in "12345678"
        ):
            raise ValueError(
                "Enter a square such as b6 or c5."
            )

        col = ord(text[0]) - ord("a")
        row = 8 - int(text[1])

        if (row + col) % 2 != 1:
            raise ValueError(
                "Choose a playable dark square."
            )

        return row, col

    def switch_player(self):
        self.current = 1 - self.current

    def finish(self, winner=None):
        self.finished = True
        self.winner = winner
        self.end_time = time.monotonic()

        for player in self.players:
            if winner is None:
                player.result = "Game ended without a winner"
            elif player == winner:
                player.result = "Winner"
            else:
                player.result = "Lost"

    def show_summary(self):
        duration = self.end_time - self.start_time

        print("\n========== GAME SUMMARY ==========")

        if self.winner:
            print("Winner:", self.winner.name)
        else:
            print("Result: Game ended without a winner")

        print("Total moves:", self.total_moves)
        print(f"Game duration: {duration:.1f} seconds")

        for player in self.players:
            print(f"\nPlayer: {player.name}")
            print("Colour:", player.color)
            print("Moves:", player.moves)
            print("Result:", player.result)
            print(f"Time in game: {player.time_played:.1f} seconds")

    def play(self):
        print("\nWelcome to Checkers!")
        print("Enter moves using coordinates, e.g. b6 a5.")
        print("Type 'finish' to end the game.")
        print("Type 'move' to make a move.")

        while not self.finished:
            player = self.current_player()
            self.board.display()

            legal = self.board.legal_moves(player.color)

            if not legal:
                self.finish(self.players[1 - self.current])
                break

            captures_required = any(
                move[2] is not None for move in legal
            )

            print(f"\nMove {self.total_moves + 1}")
            print(f"Current player: {player}, moves made: {player.moves}")

            if captures_required:
                print("A capture is compulsory.")

            if self.must_capture_from is not None:
                print(
                    "You must continue with the same checker "
                    "from its current square."
                )

            print("Enter 'move' or 'finish'.")

            turn_start = time.monotonic()

            try:
                choice = input("Your choice: ").strip().lower()

                if choice == "finish":
                    self.finish()
                    break

                if choice != "move":
                    print("Please enter 'move' or 'finish'.")
                    continue

                move_text = input(
                    "Enter source and destination (e.g. b6 a5): "
                ).split()

                if len(move_text) != 2:
                    raise ValueError(
                        "Enter exactly two squares."
                    )

                start = self.parse_square(move_text[0])
                end = self.parse_square(move_text[1])

                # Force the same checker to continue capturing.
                if (
                    self.must_capture_from is not None
                    and start != self.must_capture_from
                ):
                    raise ValueError(
                        "Continue capturing with the same checker."
                    )

                captured, promoted = self.board.move(
                    start, end, player.color
                )

                player.record_move()
                self.total_moves += 1

                print(
                    f"{player.name} moved {move_text[0]} "
                    f"to {move_text[1]}."
                )

                # Promotion during a capture ends the turn immediately.
                if captured and not promoted:
                    # Check for another capture by this checker.
                    next_captures = [
                        move
                        for move in self.board.legal_moves(player.color)
                        if move[0] == end and move[2] is not None
                    ]

                    if next_captures:
                        self.must_capture_from = end
                        continue

                # The turn ends when no further capture is required.
                self.must_capture_from = None
                self.switch_player()

            except ValueError as error:
                print("Invalid move:", error)

            finally:
                player.time_played += (
                    time.monotonic() - turn_start
                )

        self.show_summary()


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":
    print("=== CHECKERS GAME ===")

    name1 = input("Enter Player 1 name (red): ").strip()
    name2 = input("Enter Player 2 name (black): ").strip()

    if not name1:
        name1 = "Player 1"

    if not name2:
        name2 = "Player 2"

    game = Game(name1, name2)
    game.play()
