def minSubarray(nums, p):
    total_sum = sum(nums)
    target_remainder = total_sum % p

    # If the total sum is already divisible by p, return 0
    if target_remainder == 0:
        return 0

    # Check if it's impossible to find such a subarray
    if total_sum < p:
        return -1

    # Use a hashmap to track cumulative sum mod p
    current_sum = 0
    sum_index_map = {0: -1}  # To handle cases where the valid subarray starts from index 0
    min_length = float('inf')

    for i, num in enumerate(nums):
        current_sum += num
        mod_sum = current_sum % p

        # We want the previous mod sum that would yield the target remainder
        required_mod = (mod_sum - target_remainder + p) % p

        if required_mod in sum_index_map:
            # Calculate the length of the subarray to remove
            length = i - sum_index_map[required_mod]
            min_length = min(min_length, length)

        # Store the current sum mod p
        sum_index_map[mod_sum] = i

    # If we found a valid length, return it, else return -1
    return min_length if min_length != float('inf') else -1


# Test the function
nums = [1, 2, 3]
p = 7
print(minSubarray(nums, p))  # Expected output: -1
