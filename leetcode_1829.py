def getMaximumXor(nums, maximumBit):

    n = len(nums)

    # Calculate the maximum possible XOR value
    max_xor = 0
    for num in nums:
        max_xor ^= num

    # Create a bitmask to find the maximum `k` value
    bitmask = (1 << maximumBit) - 1

    # Perform the queries
    answer = []
    for i in range(n):
        # Find the maximum `k` value
        k = max_xor ^ bitmask
        answer.append(k)

        # Remove the last element from the array
        max_xor ^= nums[-1]
        nums.pop()

    return answer

print(getMaximumXor([0,1,1,3],2))
print(getMaximumXor([2,3,4,7],3))