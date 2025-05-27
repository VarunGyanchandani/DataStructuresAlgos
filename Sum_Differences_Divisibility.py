class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        num_1 = []
        num_2 = []
        for i in range(1, n + 1):
            if i % m == 0:
                num_2.append(i)
            else:
                num_1.append(i)

        for i in num_1:
            num1 += i
        for j in num_2:
            num2 += j

        return num1 - num2

sol=Solution()
print(sol.differenceOfSums(10,3))
print(sol.differenceOfSums(5,6))
print(sol.differenceOfSums(5,1))