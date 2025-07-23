class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def process_removals(text: str, sub: str, score: int):
            stack = []
            points = 0
            for char in text:
                if stack and stack[-1] == sub[0] and char == sub[1]:
                    stack.pop()
                    points += score
                else:
                    stack.append(char)

            return points, "".join(stack)

        if x > y:
            # First, remove all "ab"s.
            score1, s_after_pass1 = process_removals(s, "ab", x)
            # Then, remove all "ba"s from the remaining string.
            score2, _ = process_removals(s_after_pass1, "ba", y)
            return score1 + score2
        else:
            # First, remove all "ba"s.
            score1, s_after_pass1 = process_removals(s, "ba", y)
            # Then, remove all "ab"s from the remaining string.
            score2, _ = process_removals(s_after_pass1, "ab", x)
            return score1 + score2


def main():
    # Create instance of Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ("cdbcbbaaabab", 4, 5),  # Example with "ba" having higher points
        ("aabbaaxybbaabb", 5, 4),  # Example with "ab" having higher points
        ("aabb", 3, 3),  # Equal points case
        ("abab", 2, 1),  # Simple alternating pattern
        ("xyz", 10, 10),  # No valid pairs case
        ("aaaabbbb", 5, 2),  # No valid pairs after first pass
    ]

    # Run test cases
    for i, (s, x, y) in enumerate(test_cases, 1):
        result = solution.maximumGain(s, x, y)
        print(f"Test Case {i}:")
        print(f"Input: s = '{s}', x = {x}, y = {y}")
        print(f"Output: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()