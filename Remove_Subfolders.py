from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folder list to ensure parent folders come before sub-folders
        folder.sort()
        # Initialize result list to store non-sub-folder paths
        result = []

        # Iterate through each folder in the sorted list
        for f in folder:
            # Add folder if result is empty or if it's not a sub-folder of the last added folder
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    folder1 = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    print("Example 1 Input:", folder1)
    print("Output:", solution.removeSubfolders(folder1))  # ["/a", "/c/d", "/c/f"]

    # Example 2
    folder2 = ["/a", "/a/b/c", "/a/b/d"]
    print("Example 2 Input:", folder2)
    print("Output:", solution.removeSubfolders(folder2))  # ["/a"]

    # Example 3
    folder3 = ["/a/b/c", "/a/b/ca", "/a/b/d"]
    print("Example 3 Input:", folder3)
    print("Output:", solution.removeSubfolders(folder3))  # ["/a/b/c", "/a/b/ca", "/a/b/d"]