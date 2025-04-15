from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Find the position of each value in nums2
        pos2 = [0] * n
        for i in range(n):
            pos2[nums2[i]] = i

        # For each value in nums1, get its position in nums2
        positions = [pos2[nums1[i]] for i in range(n)]

        # Binary Indexed Tree (Fenwick Tree) for efficient range sum queries
        bit = [0] * (n + 1)

        def update(idx, val):
            while idx <= n:
                bit[idx] += val
                idx += idx & -idx

        def query(idx):
            result = 0
            while idx > 0:
                result += bit[idx]
                idx -= idx & -idx
            return result

        # Count values smaller to the left of each position
        smaller_left = [0] * n
        for i in range(n):
            smaller_left[i] = query(positions[i])
            update(positions[i] + 1, 1)

        # Reset BIT for next computation
        bit = [0] * (n + 1)

        # Count values greater to the right of each position
        result = 0
        for i in range(n - 1, -1, -1):
            greater_right = query(n) - query(positions[i])
            result += smaller_left[i] * greater_right
            update(positions[i] + 1, 1)

        return result


# Example usage with detailed tracing
def trace_example():
    sol = Solution()
    nums1 = [2, 0, 1, 3]
    nums2 = [0, 1, 2, 3]

    print("Example 1:")
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")

    # Trace the algorithm execution
    n = len(nums1)

    # Find positions in nums2
    pos2 = [0] * n
    for i in range(n):
        pos2[nums2[i]] = i

    print(f"Positions in nums2: {pos2}")
    # pos2[0] = 0, pos2[1] = 1, pos2[2] = 2, pos2[3] = 3

    # For each value in nums1, get its position in nums2
    positions = [pos2[nums1[i]] for i in range(n)]
    print(f"Reordered positions: {positions}")
    # positions = [2, 0, 1, 3]

    # Create Fenwick Tree for the first pass
    bit = [0] * (n + 1)

    # Functions for Fenwick Tree operations
    def update(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & -idx

    def query(idx):
        result = 0
        while idx > 0:
            result += bit[idx]
            idx -= idx & -idx
        return result

    # Count values smaller to the left of each position
    smaller_left = [0] * n
    print("\nComputing smaller_left:")
    for i in range(n):
        smaller_left[i] = query(positions[i])
        update(positions[i] + 1, 1)
        print(f"position[{i}] = {positions[i]}, smaller_left[{i}] = {smaller_left[i]}, BIT = {bit}")

    print(f"Final smaller_left: {smaller_left}")

    # Reset BIT for next computation
    bit = [0] * (n + 1)

    # Count values greater to the right of each position
    result = 0
    print("\nComputing greater_right and final result:")
    for i in range(n - 1, -1, -1):
        greater_right = query(n) - query(positions[i])
        contribution = smaller_left[i] * greater_right
        result += contribution
        update(positions[i] + 1, 1)
        print(f"position[{i}] = {positions[i]}, smaller_left[{i}] = {smaller_left[i]}, greater_right = {greater_right}")
        print(f"Contribution to result: {contribution}, Current result: {result}")
        print(f"BIT after update: {bit}")

    print(f"\nFinal result: {result}")

    # Verify with direct calculation
    print("\nVerification by checking all possible triplets:")
    for x in range(n):
        for y in range(x + 1, n):
            for z in range(y + 1, n):
                # Values in nums1
                val_x, val_y, val_z = nums1[x], nums1[y], nums1[z]

                # Positions in nums2
                pos_x = pos2[val_x]
                pos_y = pos2[val_y]
                pos_z = pos2[val_z]

                if pos_x < pos_y < pos_z:
                    print(f"Good triplet: ({val_x}, {val_y}, {val_z})")

    return sol.goodTriplets(nums1, nums2)


# Run example
result = trace_example()
print(f"Solution output: {result}")


# Let's also trace through Example 2
def trace_example2():
    sol = Solution()
    nums1 = [4, 0, 1, 3, 2]
    nums2 = [4, 1, 0, 2, 3]

    print("\n\nExample 2:")
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")

    # Verify with direct calculation
    n = len(nums1)
    pos2 = [0] * n
    for i in range(n):
        pos2[nums2[i]] = i

    print("\nVerification by checking all possible triplets:")
    good_triplets = []
    for x in range(n):
        for y in range(x + 1, n):
            for z in range(y + 1, n):
                # Values in nums1
                val_x, val_y, val_z = nums1[x], nums1[y], nums1[z]

                # Positions in nums2
                pos_x = pos2[val_x]
                pos_y = pos2[val_y]
                pos_z = pos2[val_z]

                if pos_x < pos_y < pos_z:
                    good_triplets.append((val_x, val_y, val_z))
                    print(f"Good triplet: ({val_x}, {val_y}, {val_z})")

    print(f"Total good triplets: {len(good_triplets)}")
    return sol.goodTriplets(nums1, nums2)


# Run second example
result2 = trace_example2()
print(f"Solution output: {result2}")