import heapq

def minimum_score_optimized(nums):
    n = len(nums)
    marked = [False] * n
    score = 0
    heap = []
    for i in range(n):
        heapq.heappush(heap, (nums[i], i))

    marked_count = 0  # Keep track of the number of marked elements
    while marked_count < n:
        val, index = heapq.heappop(heap)
        if marked[index]:
            continue

        score += val
        marked[index] = True
        marked_count += 1 #Increment the marked_count
        if index > 0 and not marked[index - 1]:
            marked[index - 1] = True
            marked_count += 1
        if index < n - 1 and not marked[index + 1]:
            marked[index + 1] = True
            marked_count += 1

    return score

print(minimum_score_optimized([2, 1, 3, 4, 5, 2]))
print(minimum_score_optimized([2, 3, 5, 1, 3, 2]))