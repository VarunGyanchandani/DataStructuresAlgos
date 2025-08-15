class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n & (n - 1) != 0:
            return False
        if n & 0xAAAAAAAA != 0:
            return False
        return True

solution = Solution()

memory_blocks = [1, 4, 8, 16, 32, 64, 100, 256, 1024]

print("Valid memory allocations (powers of 4):")
for block in memory_blocks:
    if solution.isPowerOfFour(block):
        print(f"{block} MB is valid.")
    else:
        print(f"{block} MB is NOT valid.")
