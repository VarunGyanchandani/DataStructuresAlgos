from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Builds an array 'ans' such that ans[i] = nums[nums[i]]
        using O(1) extra space.
        """
        n = len(nums)

        for i in range(n):
            # val_b_component is original_nums[nums[i]] which is retrieved by (nums[nums[i]] % n)
            val_b_component = nums[nums[i]] % n
            # nums[i] on the right is original_nums[i] (current value before this specific update)
            nums[i] = nums[i] + n * val_b_component
            # Now, nums[i] holds: original_value_of_nums_i + n * (original_value_of_nums_at_index_[original_value_of_nums_i])

        for i in range(n):
            nums[i] = nums[i] // n

        return nums

    def buildArray_extra_space(self, nums: List[int]) -> List[int]:
        """
        Builds an array 'ans' such that ans[i] = nums[nums[i]]
        using O(n) extra space.
        """
        n = len(nums)
        # Create a new list for the answer.
        # A list comprehension can make this concise.
        ans = [0] * n
        for i in range(n):
            ans[i] = nums[nums[i]]
        return ans


# --- Example Usage ---
if __name__ == "__main__":
    # Create an instance of the Solution class
    solver = Solution()

    # Example 1 from the problem description
    nums1 = [0, 2, 1, 5, 3, 4]
    print(f"Original nums1: {nums1}")

    ans1_inplace = solver.buildArray(list(nums1))  # Pass a copy if nums1 needs to be preserved for other uses
    print(f"Result from buildArray (O(1) space) for nums1: {ans1_inplace}")
    # Expected output: [0, 1, 2, 4, 5, 3]

    nums1_for_extra_space = [0, 2, 1, 5, 3, 4]
    ans1_extra_space = solver.buildArray_extra_space(nums1_for_extra_space)
    print(f"Result from buildArray_extra_space (O(n) space) for nums1: {ans1_extra_space}")
    print("-" * 30)

    # Example 2 from the problem description
    nums2 = [5, 0, 1, 2, 3, 4]
    print(f"Original nums2: {nums2}")

    # Using the O(1) space solution
    ans2_inplace = solver.buildArray(list(nums2))  # Pass a copy
    print(f"Result from buildArray (O(1) space) for nums2: {ans2_inplace}")
    # Expected output: [4, 5, 0, 1, 2, 3]

    nums2_for_extra_space = [5, 0, 1, 2, 3, 4]
    ans2_extra_space = solver.buildArray_extra_space(nums2_for_extra_space)
    print(f"Result from buildArray_extra_space (O(n) space) for nums2: {ans2_extra_space}")
    print("-" * 30)

    # Edge case: single element
    nums3 = [0]
    print(f"Original nums3: {nums3}")
    ans3_inplace = solver.buildArray(list(nums3))
    print(f"Result from buildArray (O(1) space) for nums3: {ans3_inplace}")
    # Expected output: [0] (nums[nums[0]] = nums[0] = 0)

    nums3_for_extra_space = [0]
    ans3_extra_space = solver.buildArray_extra_space(nums3_for_extra_space)
    print(f"Result from buildArray_extra_space (O(n) space) for nums3: {ans3_extra_space}")
    print("-" * 30)