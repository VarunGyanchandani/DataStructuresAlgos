def calculate_score(s):
  score = 0
  for i in range(1, len(s)):
    score += abs(ord(s[i]) - ord(s[i-1]))
  return score

print(calculate_score("hello"))  # Output: 13
print(calculate_score("zaz"))    # Output: 50
