from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) <= 1:
            return words

        result = [words[0]]

        for i in range(1, len(words)):
            current_word = words[i]
            last_added_word = result[-1]

            if sorted(current_word) != sorted(last_added_word):
                result.append(current_word)

        return result


# Function to test the removeAnagrams method with example cases
def test_remove_anagrams():
    solution = Solution()

    # Test Case 1: List with consecutive anagrams
    test1 = ["abba", "baba", "bbaa", "cd", "cd"]
    print(f"Test 1 Input: {test1}")
    print(f"Test 1 Output: {solution.removeAnagrams(test1)}")
    # Expected output: ["abba", "cd"]

    # Test Case 2: Single word
    test2 = ["hello"]
    print(f"\nTest 2 Input: {test2}")
    print(f"Test 2 Output: {solution.removeAnagrams(test2)}")
    # Expected output: ["hello"]

    # Test Case 3: Empty list
    test3 = []
    print(f"\nTest 3 Input: {test3}")
    print(f"Test 3 Output: {solution.removeAnagrams(test3)}")
    # Expected output: []

    # Test Case 4: No anagrams
    test4 = ["cat", "dog", "bird"]
    print(f"\nTest 4 Input: {test4}")
    print(f"Test 4 Output: {solution.removeAnagrams(test4)}")
    # Expected output: ["cat", "dog", "bird"]

    # Test Case 5: All anagrams
    test5 = ["tea", "eat", "ate"]
    print(f"\nTest 5 Input: {test5}")
    print(f"Test 5 Output: {solution.removeAnagrams(test5)}")
    # Expected output: ["tea"]


# Run the tests
if __name__ == "__main__":
    test_remove_anagrams()