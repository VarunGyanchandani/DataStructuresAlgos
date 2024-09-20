
def shortestPalindrome(s: str) -> str:
    if not s:
        return ""

    # Create the reversed string
    rev_s = s[::-1]

    # Create the combined string
    combined = s + "#" + rev_s

    # Create the LPS array
    lps = [0] * len(combined)
    j = 0

    # Fill the LPS array
    for i in range(1, len(combined)):
        while j > 0 and combined[i] != combined[j]:
            j = lps[j - 1]
        if combined[i] == combined[j]:
            j += 1
            lps[i] = j
        else:
            lps[i] = 0

    # The length of the longest palindromic prefix
    longest_palindromic_prefix_len = lps[-1]

    # We need to add the rest of the reversed string to the front
    to_add = rev_s[:len(s) - longest_palindromic_prefix_len]

    # Construct the shortest palindrome
    return to_add + s


print(shortestPalindrome("aacecaaa"))
print(shortestPalindrome("abcd"))