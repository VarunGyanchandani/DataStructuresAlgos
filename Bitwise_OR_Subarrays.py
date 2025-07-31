from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        prev = set()

        for num in arr:
            curr = {num}
            for prev_or in prev:
                curr.add(prev_or | num)
            result.update(curr)
            prev = curr

        return len(result)

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example input array
    arr = [1, 2, 4]

    # Calculate number of unique bitwise ORs of subarrays
    unique_or_count = solution.subarrayBitwiseORs(arr)

    # Output the result
    print(f"Number of unique bitwise ORs of subarrays: {unique_or_count}")
