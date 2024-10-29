def maxUniqueSplit(s: str) -> int:
    def backtrack(start, seen):
        if start == len(s):
            return 0

        max_unique = 0
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring not in seen:
                seen.add(substring)
                # Recurse for the rest of the string
                max_unique = max(max_unique, 1 + backtrack(end, seen))
                seen.remove(substring)

        return max_unique

    return backtrack(0, set())


# Example usage:
print(maxUniqueSplit("ababccc"))  # Output: 5
print(maxUniqueSplit("aba"))  # Output: 2
print(maxUniqueSplit("aa"))  # Output: 1