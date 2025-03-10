class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Use a sliding window with two pointers
        for left in range(n):
            # Skip if we don't have enough characters left
            if left + k + 5 > n:
                break

            vowel_count = {v: 0 for v in vowels}
            consonant_count = 0

            # Process the window
            for right in range(left, n):
                char = word[right]

                # Update counts
                if char in vowels:
                    vowel_count[char] += 1
                else:
                    consonant_count += 1

                # If too many consonants, break - no valid substrings can start at 'left'
                if consonant_count > k:
                    break

                # If exactly k consonants and all vowels present, increment count
                if (consonant_count == k and all(vowel_count[v] > 0 for v in vowels)):
                    count += 1

        return count

word = "aeioubcdfg"
k = 2
solution = Solution()
result = solution.countOfSubstrings(word, k)
print(f"Number of valid substrings: {result}")