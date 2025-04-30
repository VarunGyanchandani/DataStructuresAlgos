from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            # Convert the number to a string and count its length
            if len(str(num)) % 2 == 0:
                count += 1
        return count


def main():
    # Create instance of Solution class
    solution = Solution()

    # Example 1
    example1 = [12, 345, 2, 6, 7896]
    result1 = solution.findNumbers(example1)
    print(f"Example 1:")
    print(f"Input: nums = {example1}")
    print(f"Output: {result1}")
    print("Explanation:")
    for num in example1:
        digits = len(str(num))
        even_or_odd = "even" if digits % 2 == 0 else "odd"
        print(f"{num} contains {digits} digits ({even_or_odd} number of digits).")

    print("\n" + "-" * 50 + "\n")

    # Example 2
    example2 = [555, 901, 482, 1771]
    result2 = solution.findNumbers(example2)
    print(f"Example 2:")
    print(f"Input: nums = {example2}")
    print(f"Output: {result2}")
    print("Explanation:")
    for num in example2:
        digits = len(str(num))
        even_or_odd = "even" if digits % 2 == 0 else "odd"
        print(f"{num} contains {digits} digits ({even_or_odd} number of digits).")

    print("\n" + "-" * 50 + "\n")

    # Custom example with user input
    print("Try your own array of numbers:")
    try:
        user_input = input("Enter numbers separated by commas: ")
        user_nums = [int(x.strip()) for x in user_input.split(",")]
        user_result = solution.findNumbers(user_nums)
        print(f"Input: nums = {user_nums}")
        print(f"Output: {user_result}")
        print("Explanation:")
        for num in user_nums:
            digits = len(str(num))
            even_or_odd = "even" if digits % 2 == 0 else "odd"
            print(f"{num} contains {digits} digits ({even_or_odd} number of digits).")
    except ValueError:
        print("Invalid input. Please enter integers separated by commas.")


if __name__ == "__main__":
    main()