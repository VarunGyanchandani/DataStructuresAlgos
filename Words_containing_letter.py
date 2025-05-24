from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]

sol = Solution()
print(sol.findWordsContaining(["leet","code"], "e"))     # Output: [0, 1]
print(sol.findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))  # Output: [0, 2]
print(sol.findWordsContaining(["abc","bcd","aaaa","cbc"], "z"))  # Output: []
