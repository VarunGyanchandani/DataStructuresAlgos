def minPenalty(nums, maxOperations):
    def canAchieveMaxSize(maxSize):
        splits_needed = 0
        for balls in nums:
            if balls > maxSize:
                # Calculate the number of splits needed to make all parts <= maxSize
                splits_needed += (balls - 1) // maxSize
            if splits_needed > maxOperations:
                return False
        return True

    # Binary search to find the minimum possible maximum bag size
    left, right = 1, max(nums)

    while left < right:
        mid = (left + right) // 2
        if canAchieveMaxSize(mid):
            right = mid  # Try for a smaller max size
        else:
            left = mid + 1  # Increase the max size

    return left

print(minPenalty([9],2))
print(minPenalty([2,4,8,2],4))