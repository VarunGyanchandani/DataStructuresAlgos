class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Process from right to left (most significant to least significant)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        # Convert to string, skipping leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))


# Example usage
solution = Solution()

num1 = "123"
num2 = "456"
result = solution.multiply(num1, num2)
print(f"Multiplication of {num1} and {num2} is: {result}")
