class Solution:
    def clearDigits(self, s: str) -> str:
        s_list = list(s)
        while True:
            digit_index = -1
            for i in range(len(s_list)):
                if s_list[i].isdigit():
                    digit_index = i
                    break
            if digit_index == -1:
                break

            non_digit_index = -1
            for i in range(digit_index - 1, -1, -1):
                if not s_list[i].isdigit():
                    non_digit_index = i
                    break

            if non_digit_index != -1:
                if non_digit_index < digit_index:
                    del s_list[digit_index]
                    del s_list[non_digit_index]
                else: # This should not happen, but for safety.
                    del s_list[digit_index]
            else:
                del s_list[digit_index]

        return "".join(s_list)

solution = Solution()
input_string = "cb34"
result = solution.clearDigits(input_string)
print(f"Input: '{input_string}', Output: '{result}'")

input_string2 = "abc"
result2 = solution.clearDigits(input_string2)
print(f"Input: '{input_string2}', Output: '{result2}'")

input_string3 = "axb12c3"
result3 = solution.clearDigits(input_string3)
print(f"Input: '{input_string3}', Output: '{result3}'")