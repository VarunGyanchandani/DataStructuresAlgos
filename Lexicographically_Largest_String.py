class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        from functools import lru_cache

        n = len(word)
        max_word = ""

        @lru_cache(None)
        def dfs(start: int, parts_left: int):
            nonlocal max_word
            if parts_left == 1:
                part = word[start:]
                max_word = max(max_word, part)
                return [[part]]

            splits = []
            for i in range(start + 1, n - parts_left + 2):
                left = word[start:i]
                max_word = max(max_word, left)
                for rest in dfs(i, parts_left - 1):
                    splits.append([left] + rest)
            return splits

        dfs(0, numFriends)
        return max_word


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    word1 = "dbca"
    numFriends1 = 2
    result1 = solution.answerString(word1, numFriends1)
    print(f"Input: word = '{word1}', numFriends = {numFriends1}")
    print(f"Output: '{result1}'")  # Expected: "dbc"

    # Example 2
    word2 = "gggg"
    numFriends2 = 4
    result2 = solution.answerString(word2, numFriends2)
    print(f"Input: word = '{word2}', numFriends = {numFriends2}")
    print(f"Output: '{result2}'")  # Expected: "g"

    # Additional test case
    word3 = "zxyabc"
    numFriends3 = 3
    result3 = solution.answerString(word3, numFriends3)
    print(f"Input: word = '{word3}', numFriends = {numFriends3}")
    print(f"Output: '{result3}'")  # Example output may be "zxy", "z", or "abc" depending on the splits
