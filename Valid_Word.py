import collections

class Solution:

    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False
        vowels = "aeiouAEIOU"

        for char in word:

            if not char.isalnum():
                return False

            if char.isalpha():

                if char in vowels:
                    has_vowel = True

                else:
                    has_consonant = True

        return has_vowel and has_consonant


solver = Solution()

word1 = "234Adas"
print(f"Is the word '{word1}' valid? 👉 {solver.isValid(word1)}")

word2 = "b3"
print(f"Is the word '{word2}' valid? 👉 {solver.isValid(word2)}")

word3 = "a3$e"
print(f"Is the word '{word3}' valid? 👉 {solver.isValid(word3)}")
