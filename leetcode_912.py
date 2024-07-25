from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            # Divide the array into two halves
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Recursively sort each half
            left_sorted = merge_sort(left_half)
            right_sorted = merge_sort(right_half)

            # Merge the sorted halves
            return merge(left_sorted, right_sorted)

        # Helper function to merge two sorted arrays
        def merge(left, right):
            sorted_arr = []
            i = j = 0

            # Merge both halves into the sorted_arr
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1

            # Append remaining elements
            while i < len(left):
                sorted_arr.append(left[i])
                i += 1
            while j < len(right):
                sorted_arr.append(right[j])
                j += 1

            return sorted_arr

        # Call merge sort on the input array
        return merge_sort(nums)