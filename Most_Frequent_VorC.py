from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        freq = Counter(s)

        # Find the maximum frequency of vowels and consonants
        max_vowel = max((count for ch, count in freq.items() if ch in vowels), default=0)
        max_consonant = max((count for ch, count in freq.items() if ch not in vowels), default=0)

        # Return the sum of max frequencies
        return max_vowel + max_consonant


solution = Solution()

input_string = "successes"

result = solution.maxFreqSum(input_string)

# Output the result
print(f"Sum of the maximum frequencies of vowels and consonants in '{input_string}': {result}")
