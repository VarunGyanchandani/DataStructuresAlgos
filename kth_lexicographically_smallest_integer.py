# kth_lexicographical_number.py

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        while k > 0:
            count = 0
            first = current
            last = current + 1

            while first <= n:
                count += min(n + 1, last) - first
                first *= 10
                last *= 10

            if count <= k:
                current += 1
                k -= count
            else:
                current *= 10
                k -= 1

        return current


# Example usage
def main():
    solver = Solution()

    examples = [
        (13, 2),  # Expected output: 10
        (1, 1),  # Expected output: 1
        (100, 10),  # Additional case: should give 17
        (1000, 100),  # Large range
    ]

    for n, k in examples:
        result = solver.findKthNumber(n, k)
        print(f"n = {n}, k = {k} => kth smallest: {result}")


if __name__ == "__main__":
    main()
