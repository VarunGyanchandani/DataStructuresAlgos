class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings by the dot (.) and convert them to integers
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.')))

        # Make sure both version lists have the same length by appending zeroes
        max_len = max(len(v1_parts), len(v2_parts))
        v1_parts.extend([0] * (max_len - len(v1_parts)))
        v2_parts.extend([0] * (max_len - len(v2_parts)))

        # Compare the parts of each version
        for a, b in zip(v1_parts, v2_parts):
            if a < b:
                return -1  # version1 is older
            elif a > b:
                return 1  # version1 is newer
        return 0  # versions are the same


solution = Solution()

version1 = "1.2.0"
version2 = "1.2.1"

result = solution.compareVersion(version1, version2)

if result == -1:
    print(f"Version {version1} is older than version {version2}.")
elif result == 1:
    print(f"Version {version1} is newer than version {version2}.")
else:
    print(f"Version {version1} and version {version2} are the same.")
