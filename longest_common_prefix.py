def longestCommonPrefix(strs):


  if not strs:  # Handle empty list case
    return ""

  prefix = strs[0]  # Initialize prefix with the first string
  for string in strs[1:]:  # Iterate through remaining strings
    while prefix not in string[:len(prefix)]:  # Check if prefix is present at the beginning
      prefix = prefix[:-1]  # Reduce prefix length if mismatch found
      if not prefix:  # Return empty string if no common prefix exists
        return ""
  return prefix

# Example usage
strs = ["flower", "flow", "flight"]
longest_prefix = longestCommonPrefix(strs)
print(longest_prefix)  # Output: "fl"

strs = ["dog", "racecar", "car"]
longest_prefix = longestCommonPrefix(strs)
print(longest_prefix)  # Output: ""
