def common_prefix_length(s1, s2):
    # Function to find the common prefix length between two strings
    min_length = min(len(s1), len(s2))
    for i in range(min_length):
        if s1[i] != s2[i]:
            return i
    return min_length


def longest_common_prefix(arr1, arr2):
    # Convert numbers to strings
    str_arr1 = [str(num) for num in arr1]
    str_arr2 = [str(num) for num in arr2]

    max_length = 0

    # Compare each number in arr1 with each number in arr2
    for str_x in str_arr1:
        for str_y in str_arr2:
            # Calculate the common prefix length
            length = common_prefix_length(str_x, str_y)
            max_length = max(max_length, length)

    return max_length


# Example Usage
arr1 = [1, 3]
arr2 = [32, 22]
print(longest_common_prefix(arr1, arr2))  # Output: 1

arr1 = [1, 10, 100]
arr2 = [1000]
print(longest_common_prefix(arr1, arr2))  # Output: 3

arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(longest_common_prefix(arr1, arr2))  # Output: 0
