# subsequence and contiguous subarray
arr1 = [3, -1, 5, -100, 4, 2]
sum = 0
max = -1e8
i = 0
while i < len(arr1):
    sum += arr1[i]
    if sum > max:
        max = sum
    if sum < 0:
        sum = 0
    i = i+1

print(max)
