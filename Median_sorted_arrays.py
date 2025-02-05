class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the shorter array to minimize the binary search steps
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            # Partition nums1 at position i
            i = (imin + imax) // 2
            # Corresponding partition in nums2
            j = half_len - i

            # Check if elements around the partition are in order
            if i < m and nums2[j - 1] > nums1[i]:
                # Increase i to move the partition in nums1 to the right
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # Decrease i to move the partition in nums1 to the left
                imax = i - 1
            else:
                # Correct partition found, calculate max of left part
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                # If total length is odd, return max_left as the median
                if (m + n) % 2 == 1:
                    return max_left

                # Calculate min of right part
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                # If total length is even, return average of max_left and min_right
                return (max_left + min_right) / 2.0

        return 0.0  # This return is a fallback and should never be reached due to problem constraints

solution = Solution()
nums1 = [1, 3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.5

