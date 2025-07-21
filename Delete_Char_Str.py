class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        result_chars = []
        for char in s:
            if len(result_chars) >= 2 and result_chars[-1] == char and result_chars[-2] == char:
                continue
            result_chars.append(char)

        return "".join(result_chars)


# Example usage
if __name__ == "__main__":
    sol = Solution()

    examples = [
        "heyyy thereeee!!!",
        "woooow",
        "noooooooo",
        "yessssirrrr",
        "lookkk attt thattt"
    ]

    for original in examples:
        cleaned = sol.makeFancyString(original)
        print(f"Original: {original}  ->  Cleaned: {cleaned}")
