nums = [2, 7, 4, 16, 3, 8, 11]
target = 10
a_sum = 0

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == target:
            print(nums[i], nums[j])
