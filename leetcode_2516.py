def takeCharacters( s: str, k: int) -> int:
    # Count total occurrences of a, b, c
    total_a = s.count('a')
    total_b = s.count('b')
    total_c = s.count('c')

    # If any character's count is less than k, return -1
    if total_a < k or total_b < k or total_c < k:
        return -1

    # Sliding window to find the minimum substring to remove
    n = len(s)
    max_window = 0
    a_count = b_count = c_count = 0

    # Sliding window to track character counts in the current window
    left = 0
    for right in range(n):
        # Count characters in the current window
        if s[right] == 'a':
            a_count += 1
        elif s[right] == 'b':
            b_count += 1
        elif s[right] == 'c':
            c_count += 1

        # Shrink window if we exceed target counts
        while a_count > total_a - k or b_count > total_b - k or c_count > total_c - k:
            if s[left] == 'a':
                a_count -= 1
            elif s[left] == 'b':
                b_count -= 1
            elif s[left] == 'c':
                c_count -= 1
            left += 1

        # Update maximum valid window
        max_window = max(max_window, right - left + 1)

    # Return total length minus maximum window length
    return n - max_window

print(takeCharacters("aabaaaacaabc",2))