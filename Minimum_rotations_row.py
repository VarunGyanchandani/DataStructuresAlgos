from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        # Try making all tops equal to tops[0]
        rotations_top = self.check_rotations(tops[0], tops, bottoms, n)

        # Try making all tops equal to bottoms[0]
        rotations_bottom = self.check_rotations(bottoms[0], tops, bottoms, n)

        # Try making all bottoms equal to tops[0]
        rotations_top_for_bottom = self.check_rotations(tops[0], bottoms, tops, n)

        # Try making all bottoms equal to bottoms[0]
        rotations_bottom_for_bottom = self.check_rotations(bottoms[0], bottoms, tops, n)

        # Find the minimum valid rotation count
        min_rotations = float('inf')
        for rotation in [rotations_top, rotations_bottom, rotations_top_for_bottom, rotations_bottom_for_bottom]:
            if rotation != -1:
                min_rotations = min(min_rotations, rotation)

        return min_rotations if min_rotations != float('inf') else -1

    def check_rotations(self, target: int, primary: List[int], secondary: List[int], length: int) -> int:
        """
        Check how many rotations are needed to make all values in primary equal to target.
        Returns -1 if it's not possible.
        """
        rotations = 0
        for i in range(length):
            if primary[i] == target:
                # Already matches, no rotation needed
                continue
            elif secondary[i] == target:
                # Can be rotated to match
                rotations += 1
            else:
                # Can't make this position match the target
                return -1

        return rotations


def visualize_dominoes(tops, bottoms, rotated_indices=None):
    """
    Visualize the dominoes in ASCII art, marking rotated ones
    """
    if rotated_indices is None:
        rotated_indices = []

    n = len(tops)
    top_line = []
    bottom_line = []
    markers = []

    for i in range(n):
        if i in rotated_indices:
            top_line.append(str(bottoms[i]))
            bottom_line.append(str(tops[i]))
            markers.append("R")  # Rotated
        else:
            top_line.append(str(tops[i]))
            bottom_line.append(str(bottoms[i]))
            markers.append(" ")  # Not rotated

    print("┌─┐ " * n)
    print("│" + "│ │".join(top_line) + "│")
    print("├─┤ " * n)
    print("│" + "│ │".join(bottom_line) + "│")
    print("└─┘ " * n)
    print(" " + "  ".join(markers))
    print("R = Rotated domino")


def display_solution(tops, bottoms):
    """
    Solve the domino rotation problem and display the solution
    """
    print(f"Original dominoes:")
    visualize_dominoes(tops, bottoms)

    solution = Solution()
    min_rotations = solution.minDominoRotations(tops, bottoms)

    if min_rotations == -1:
        print("\nIt's not possible to make all tops or all bottoms the same.")
        return

    # Find which configuration gives the minimum rotations
    rotated_indices = []
    target_value = None
    is_top_row = True

    # Check if making tops all equal to tops[0] is optimal
    rotations = solution.check_rotations(tops[0], tops, bottoms, len(tops))
    if rotations != -1 and rotations == min_rotations:
        target_value = tops[0]
        is_top_row = True
        for i in range(len(tops)):
            if tops[i] != target_value and bottoms[i] == target_value:
                rotated_indices.append(i)

    # Check if making tops all equal to bottoms[0] is optimal
    elif solution.check_rotations(bottoms[0], tops, bottoms, len(tops)) == min_rotations:
        target_value = bottoms[0]
        is_top_row = True
        for i in range(len(tops)):
            if tops[i] != target_value and bottoms[i] == target_value:
                rotated_indices.append(i)

    # Check if making bottoms all equal to tops[0] is optimal
    elif solution.check_rotations(tops[0], bottoms, tops, len(tops)) == min_rotations:
        target_value = tops[0]
        is_top_row = False
        for i in range(len(tops)):
            if bottoms[i] != target_value and tops[i] == target_value:
                rotated_indices.append(i)

    # Check if making bottoms all equal to bottoms[0] is optimal
    else:
        target_value = bottoms[0]
        is_top_row = False
        for i in range(len(tops)):
            if bottoms[i] != target_value and tops[i] == target_value:
                rotated_indices.append(i)

    print(f"\nOptimal solution: {min_rotations} rotation(s)")
    print(f"Making all {'tops' if is_top_row else 'bottoms'} equal to {target_value}")
    print(f"Rotating dominoes at positions: {rotated_indices}")

    # Display the solution
    rotated_tops = tops.copy()
    rotated_bottoms = bottoms.copy()
    for i in rotated_indices:
        rotated_tops[i], rotated_bottoms[i] = rotated_bottoms[i], rotated_tops[i]

    print("\nAfter rotations:")
    visualize_dominoes(rotated_tops, rotated_bottoms, rotated_indices)


# Example 1
print("Example 1:")
tops1 = [2, 1, 2, 4, 2, 2]
bottoms1 = [5, 2, 6, 2, 3, 2]
display_solution(tops1, bottoms1)

print("\n" + "-" * 50 + "\n")

# Example 2
print("Example 2:")
tops2 = [3, 5, 1, 2, 3]
bottoms2 = [3, 6, 3, 3, 4]
display_solution(tops2, bottoms2)

print("\n" + "-" * 50 + "\n")

# Additional example
print("Additional example:")
tops3 = [1, 2, 1, 1, 1, 1]
bottoms3 = [1, 6, 2, 2, 2, 2]
display_solution(tops3, bottoms3)