class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best_char = ''
        n = len(num)
        for i in range(n - 2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i] == '9':
                    return "999"
                if num[i] > best_char:
                    best_char = num[i]
        return best_char * 3

sol = Solution()

num1 = "6777133339"
print(sol.largestGoodInteger(num1))

num2 = "2300019"
print(sol.largestGoodInteger(num2))

num3 = "42352338"
print(sol.largestGoodInteger(num3))

num4 = "999111"
print(sol.largestGoodInteger(num4))
