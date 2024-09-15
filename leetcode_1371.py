def findTheLongestSubstring(s: str) -> int:
    # Map to store the first occurrence of each bitmask
    first_occurrence = {0: -1}  # Start with bitmask 0 at index -1
    bitmask = 0  # Initial bitmask
    max_length = 0  # Maximum length of substring with all vowels even

    # Define vowel to bitmask mapping
    vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

    for i, char in enumerate(s):
        # Update bitmask if current character is a vowel
        if char in vowel_to_bit:
            bitmask ^= vowel_to_bit[char]

        # Check if this bitmask has been seen before
        if bitmask in first_occurrence:
            # Calculate the length of the substring
            length = i - first_occurrence[bitmask]
            max_length = max(max_length, length)
        else:
            # Store the first occurrence of this bitmask
            first_occurrence[bitmask] = i

    return max_length


# Example usage
print(findTheLongestSubstring("eleetminicoworoep"))  # Output: 13
print(findTheLongestSubstring("leetcodeisgreat"))  # Output: 5
print(findTheLongestSubstring("bcbcbc"))  # Output: 6
