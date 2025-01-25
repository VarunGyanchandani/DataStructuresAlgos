def lexicographicallySmallestArray(nums, limit):
    n = len(nums)
    # Create pairs of (number, original index)
    indexed = [(num, i) for i, num in enumerate(nums)]
    # Sort by values
    indexed.sort()

    # Group numbers that can be swapped with each other
    groups = []
    current_group = [indexed[0]]

    for i in range(1, n):
        # If difference between adjacent numbers <= limit,
        # they belong to same group
        if indexed[i][0] - indexed[i - 1][0] <= limit:
            current_group.append(indexed[i])
        else:
            groups.append(current_group)
            current_group = [indexed[i]]
    groups.append(current_group)


    result = [0] * n
    for group in groups:
        values = sorted([pair[0] for pair in group])
        indices = sorted([pair[1] for pair in group])

        # Assign values to indices
        for val, idx in zip(values, indices):
            result[idx] = val

    return result

print(lexicographicallySmallestArray([1,5,3,9,8],2))
print(lexicographicallySmallestArray([1,7,28,19,10],3))
