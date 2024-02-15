def findLargestSublist(nums):

    d = {}

    d[0] = -1

    length = 0

    ending_index = -1

    total = 0

    for i in range(len(nums)):

        total += -1 if (nums[i] == 0) else 1

        if total in d:
            if length < i - d.get(total):
                length = i - d.get(total)
                ending_index = i

        else:
            d[total] = i

    if ending_index != -1:
        print((ending_index - length + 1, ending_index))
    else:
        print('No sublist exists')


if __name__ == '__main__':
    nums = [0, 0, 1, 0, 1, 0, 0]
    findLargestSublist(nums)