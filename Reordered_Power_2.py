class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Precompute digit patterns of all powers of 2 within constraint
        power2_digits = {''.join(sorted(str(1 << i))) for i in range(31)}
        # Check if n's digit pattern matches any
        return ''.join(sorted(str(n))) in power2_digits


if __name__ == "__main__":
    solver = Solution()
    examples = [1, 10, 46, 128, 256, 821, 1024, 4096, 123]
    for num in examples:
        result = solver.reorderedPowerOf2(num)
        print(f"n = {num}, can be reordered to power of 2? {result}")
