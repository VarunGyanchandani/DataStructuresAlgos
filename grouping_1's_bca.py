def minSwaps(nums):
    n = len(nums)
    total_ones = sum(nums)

    if total_ones <= 1:
        return 0

    # Extend the array to handle the circular nature
    extended_nums = nums + nums

    # Initial count of 1's in the first window
    current_window_count = sum(extended_nums[:total_ones])
    max_ones_in_window = current_window_count

    # Sliding window to find the maximum number of 1's in any window of length total_ones
    for i in range(1, n):
        # Remove the element going out of the window and add the new element coming into the window
        current_window_count += extended_nums[i + total_ones - 1] - extended_nums[i - 1]
        max_ones_in_window = max(max_ones_in_window, current_window_count)

    # Minimum swaps needed to group all 1's together
    return total_ones - max_ones_in_window


# Example usage
print(minSwaps([0, 1, 0, 1, 1, 0, 0]))  # Output: 1
print(minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))  # Output: 2
print(minSwaps([1, 1, 0, 0, 1]))  # Output: 0
