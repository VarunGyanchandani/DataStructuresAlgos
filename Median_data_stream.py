import heapq

class Solution:
    def getMedian(self, arr):
        # Initialize result array and heaps
        result = []
        # maxHeap for lower half (negated values for max heap simulation)
        left = []
        # minHeap for upper half
        right = []

        def addNum(num):
            # Add to maxHeap first
            heapq.heappush(left, -num)

            # Make sure every num in left <= every num in right
            if left and right and (-left[0] > right[0]):
                val = -heapq.heappop(left)
                heapq.heappush(right, val)

            # Handle uneven size
            while len(left) > len(right) + 1:
                val = -heapq.heappop(left)
                heapq.heappush(right, val)
            while len(right) > len(left):
                val = heapq.heappop(right)
                heapq.heappush(left, -val)

        def findMedian():
            if len(left) > len(right):
                return float(-left[0])
            else:
                return (float(-left[0]) + float(right[0])) / 2.0

        # Process each number in the stream
        for num in arr:
            addNum(num)
            result.append(findMedian())

        return result

# Example usage
solution = Solution()
arr = [5, 15, 1, 3]
medians = solution.getMedian(arr)
print("Medians at each step:", medians)
