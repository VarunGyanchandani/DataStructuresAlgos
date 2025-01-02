def secondLargest(arr):
    max1 = -1
    max2 = -1

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif max1 > num > max2:
            max2 = num

    return max2 if max2 != -1 else -1


print(secondLargest([12, 35, 1, 10, 34, 1]))
print(secondLargest([10, 5, 10]))
print(secondLargest([10, 10, 10]))

