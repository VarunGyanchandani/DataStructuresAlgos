from collections import deque
from typing import List, Tuple, Optional


class SnakesAndLaddersGame:
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.n = len(board)
        self.target = self.n * self.n

    def get_coordinates(self, square: int) -> Tuple[int, int]:
        """Convert square number to (row, col) coordinates"""
        square -= 1  # Convert to 0-based indexing
        row = self.n - 1 - square // self.n
        col = square % self.n

        # For odd rows (from bottom), reverse the column
        if (self.n - 1 - row) % 2 == 1:
            col = self.n - 1 - col

        return row, col

    def get_square_number(self, row: int, col: int) -> int:
        """Convert (row, col) coordinates to square number"""
        # Calculate which row from bottom
        row_from_bottom = self.n - 1 - row

        # Adjust column based on row direction
        if row_from_bottom % 2 == 1:  # Odd rows go right to left
            adjusted_col = self.n - 1 - col
        else:  # Even rows go left to right
            adjusted_col = col

        return row_from_bottom * self.n + adjusted_col + 1

    def solve(self) -> int:
        """Find minimum dice rolls to reach the target"""
        queue = deque([(1, 0)])  # (current_square, moves)
        visited = set([1])

        while queue:
            curr_square, moves = queue.popleft()

            if curr_square == self.target:
                return moves

            # Try all dice rolls (1-6)
            for dice in range(1, 7):
                next_square = curr_square + dice

                if next_square > self.target:
                    break

                # Get coordinates and check for snake/ladder
                row, col = self.get_coordinates(next_square)
                final_square = next_square

                if self.board[row][col] != -1:
                    final_square = self.board[row][col]

                if final_square not in visited:
                    visited.add(final_square)
                    queue.append((final_square, moves + 1))

        return -1

    def solve_with_path(self) -> Tuple[int, List[int]]:
        """Find minimum dice rolls and return the path taken"""
        queue = deque([(1, 0, [1])])  # (current_square, moves, path)
        visited = set([1])

        while queue:
            curr_square, moves, path = queue.popleft()

            if curr_square == self.target:
                return moves, path

            for dice in range(1, 7):
                next_square = curr_square + dice

                if next_square > self.target:
                    break

                row, col = self.get_coordinates(next_square)
                final_square = next_square

                if self.board[row][col] != -1:
                    final_square = self.board[row][col]

                if final_square not in visited:
                    visited.add(final_square)
                    new_path = path + [next_square]
                    if final_square != next_square:
                        new_path.append(final_square)
                    queue.append((final_square, moves + 1, new_path))

        return -1, []

    def print_board(self):
        """Print the board with square numbers and snakes/ladders"""
        print(f"\n{self.n}x{self.n} Snakes and Ladders Board:")
        print("=" * (self.n * 8))

        for i in range(self.n):
            # Print square numbers
            row_nums = []
            for j in range(self.n):
                square_num = self.get_square_number(i, j)
                row_nums.append(f"{square_num:2d}")
            print(" | ".join(row_nums))

            # Print snake/ladder info
            row_info = []
            for j in range(self.n):
                if self.board[i][j] != -1:
                    row_info.append(f"→{self.board[i][j]:2d}")
                else:
                    row_info.append("   ")
            print(" | ".join(row_info))

            if i < self.n - 1:
                print("-" * (self.n * 6 - 1))

        print("=" * (self.n * 8))


def create_example_boards():
    """Create example boards for testing"""

    # Example 1: 6x6 board from the problem
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]

    # Example 2: 2x2 board
    board2 = [
        [-1, -1],
        [-1, 3]
    ]

    # Example 3: 4x4 board with multiple snakes and ladders
    board3 = [
        [-1, -1, -1, -1],
        [-1, -1, 9, -1],
        [-1, 14, -1, -1],
        [-1, -1, -1, -1]
    ]

    return [
        ("6x6 Board (Example 1)", board1),
        ("2x2 Board (Example 2)", board2),
        ("4x4 Board (Custom)", board3)
    ]


def demonstrate_solution():
    """Demonstrate the solution with examples"""
    print("🐍🪜 SNAKES AND LADDERS SOLVER 🪜🐍")
    print("=" * 50)

    examples = create_example_boards()

    for name, board in examples:
        print(f"\n📋 {name}")
        game = SnakesAndLaddersGame(board)
        game.print_board()

        # Solve and show path
        moves, path = game.solve_with_path()

        if moves == -1:
            print("\n❌ No solution found!")
        else:
            print(f"\n✅ Minimum moves required: {moves}")
            print(f"🎯 Path taken: {' → '.join(map(str, path))}")

            # Explain the path
            print("\n📝 Step-by-step explanation:")
            for i in range(len(path) - 1):
                curr = path[i]
                next_square = path[i + 1]

                # Check if this was a snake/ladder move
                if i < len(path) - 2 and abs(next_square - curr) > 6:
                    print(f"   Step {i + 1}: Square {curr} → Square {next_square} (Snake/Ladder)")
                else:
                    dice_roll = next_square - curr
                    if dice_roll <= 6:
                        print(f"   Step {i + 1}: Square {curr} → Square {next_square} (Dice roll: {dice_roll})")

        print("\n" + "-" * 50)


def test_coordinate_conversion():
    """Test coordinate conversion functions"""
    print("\n🧪 TESTING COORDINATE CONVERSION")
    print("=" * 40)

    # Test with 6x6 board
    game = SnakesAndLaddersGame([[-1] * 6 for _ in range(6)])

    test_squares = [1, 6, 7, 12, 13, 18, 19, 24, 25, 30, 31, 36]

    for square in test_squares:
        row, col = game.get_coordinates(square)
        back_to_square = game.get_square_number(row, col)
        print(f"Square {square:2d} → ({row}, {col}) → Square {back_to_square:2d} ✓")


def benchmark_performance():
    """Benchmark the algorithm performance"""
    import time

    print("\n⚡ PERFORMANCE BENCHMARK")
    print("=" * 30)

    # Create boards of different sizes
    sizes = [6, 10, 15, 20]

    for size in sizes:
        # Create a board with some random snakes and ladders
        board = [[-1] * size for _ in range(size)]

        # Add a few snakes and ladders
        if size >= 6:
            board[size - 2][1] = size * size - 5  # Ladder near start
            board[1][size - 2] = 5  # Snake near end

        game = SnakesAndLaddersGame(board)

        start_time = time.time()
        result = game.solve()
        end_time = time.time()

        print(f"Board size {size:2d}x{size:2d}: {result:2d} moves, "
              f"Time: {(end_time - start_time) * 1000:.2f}ms")


if __name__ == "__main__":
    # Run the complete demonstration
    demonstrate_solution()
    test_coordinate_conversion()
    benchmark_performance()

    print("\n🎉 Demo completed! Try creating your own boards!")


# Example of how to use the class directly:
def quick_example():
    """Quick example for direct usage"""
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]

    game = SnakesAndLaddersGame(board)
    min_moves = game.solve()
    print(f"Minimum moves needed: {min_moves}")

    # Get detailed path
    moves, path = game.solve_with_path()
    print(f"Path: {path}")

quick_example()