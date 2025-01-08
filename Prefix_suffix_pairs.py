def countPairs(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                count += 1
    return count

words1 = ["a", "aba", "ababa", "aa"]
print(countPairs(words1))  # Output: 4

words2 = ["pa", "papa", "ma", "mama"]
print(countPairs(words2))  # Output: 2

words3 = ["abab", "ab"]
print(countPairs(words3))  # Output: 0
